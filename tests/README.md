# Tests

How agents write and maintain tests. Policy lock: [PROCESS.md](../docs/PROCESS.md) § Tests.
CI unfold at the bottom stays dormant.

```text
tests/
  conftest.py        # maximize-on-one-screen; no-op when Qt is absent
  window_policy.py   # pure screen / headless decisions (no Qt)
  unit/              # fast, isolated, no network and no database
  smoke/             # app boots and the critical path is alive
  integration/       # real local services; skip cleanly when the service is down
  regression/        # full broad suite: slow, UI, and end-to-end
```

## Agent duty

Every new feature ships with a test. Every bug fix ships with a test. The bug-fix test is written first and fails because it reproduces the bug; the fix turns that test green.

When an agent edits a function that has no test, it adds at least a **characterization test** in the same change: a test that records what the code does today, and passes against that code, before the edit. If today's behavior is the bug, use the bug-fix rule instead (the new test fails first).

**Adopting an existing codebase** into this template. The first testing task, before new features:

1. A **smoke** test that the app starts (process comes up, main window constructs, or `main` returns).
2. A **capture script** on the smoke tier (GUI PNGs, or console text). See [Capture on adoption](#capture-on-adoption).
3. **Unit** tests for the core logic.

Each later change grows coverage. The first commit does not boil the ocean.

## Which tier

| Tier | Put the test here when | Stays out |
|------|------------------------|-----------|
| **unit** | The check is fast and isolated. Default pre-push run. | Network, database, a real window, the wall clock. |
| **smoke** | The app boots and the critical path is alive. GUI apps also keep a screenshot capture. Console and TUI apps keep a text capture. | Branch-level business rules. Those belong in unit tests. |
| **integration** | The check needs a real local service (database, queue, local HTTP). Mark `@pytest.mark.integration` and `pytest.skip` with a reason when that service is down. | Live vendor calls. Those are `@pytest.mark.network` and stay out of the default run. |
| **regression** | The check is the full broad suite: slow, UI, or end-to-end. Re-run to catch things that used to work breaking. Mark `@pytest.mark.regression`. | A fast isolated rule (unit) or a boot check (smoke). |

A new behavior gets a unit test unless the only risk is the shell starting.

### Run order (fail-fast)

Run the tiers in this order: **unit**, **smoke**, **integration**, **regression**. If any test in a tier fails, stop before the next tier and say which tier stopped the run.

**Regression** is the full broad suite, including slow, UI, and end-to-end checks. Re-run it to catch things that used to work breaking.

Use the project interpreter. From the repo root, `&&` and the `if` stop the next tier. A missing tier folder, or a folder with no tests, also makes pytest exit non-zero, so the chain stops:

```bash
.venv/bin/python -m pytest tests/unit -q && \
.venv/bin/python -m pytest tests/smoke -q && \
.venv/bin/python -m pytest tests/integration -q && \
.venv/bin/python -m pytest tests/regression -q
```

```powershell
.\.venv\Scripts\python.exe -m pytest tests/unit -q; if ($LASTEXITCODE -ne 0) { exit }
.\.venv\Scripts\python.exe -m pytest tests/smoke -q; if ($LASTEXITCODE -ne 0) { exit }
.\.venv\Scripts\python.exe -m pytest tests/integration -q; if ($LASTEXITCODE -ne 0) { exit }
.\.venv\Scripts\python.exe -m pytest tests/regression -q; if ($LASTEXITCODE -ne 0) { exit }
```

## Isolation (no leaked state)

**Leaked state** (a **state leak**) is anything one test leaves behind that changes another test's result. Definition: [Glossary](../docs/Glossary.md). Symptom: a test passes alone and fails in the full suite, or the other way around.

| What one test might leave behind | What you do |
|----------------------------------|-------------|
| Module globals, singletons, caches | Build a fresh object inside the test, or reset the global in teardown. |
| Open windows, widgets, timers, threads | Close and `deleteLater` the widgets in teardown. Stop timers and join threads there too. The window fixture is a backstop, not a substitute. |
| `os.environ`, `PATH` | Change them with `monkeypatch` so the next test sees the original values. Never append to `PATH` in a way that survives the test. |
| Files | Write under `tmp_path`. Remove anything written outside it. |
| Database rows | Insert under a unique key this test owns, and delete that key in teardown. The test still passes when the table starts empty. It does not read a row a previous run left behind. |
| Mocks and patches | Undo them (`monkeypatch`, or the mock's own stop) before the test returns. |
| Current working directory | `monkeypatch.chdir(...)`. The process returns to the directory it started in. |
| Wall clock or network | Pass time in as an argument. Mark `network` or `integration` when the test really must use the clock or the network. |

```python
def test_flag_selects_local_mode(monkeypatch: pytest.MonkeyPatch) -> None:
    """monkeypatch: restores FEATURE_MODE after the test so the environment does not grow.

    FEATURE_MODE: the switch under test. The value lives only for this test.
    """
    monkeypatch.setenv("FEATURE_MODE", "local")
    assert mode_from_env() == "local"
```

```python
@pytest.mark.integration
def test_stores_its_own_row() -> None:
    """Insert one row under a key this test owns, then delete that key.

    The key is unique to this test. Teardown removes it even when the assert fails.
    Skip with a reason when the local service is down. The unit tier does not need it.
    """
    if not service_is_up():
        pytest.skip("local service is down")
    key = f"test-{uuid4()}"
    try:
        store.put(key, "value")
        assert store.get(key) == "value"
    finally:
        store.delete(key)
```

## GUI and RPA windows

Top-level test windows open **maximized**, on **one screen**: the primary screen, or the screen named by `TEST_SCREEN` (blank means primary). A test that needs an exact size opts out:

```python
@pytest.mark.windowed
def test_dialog_keeps_its_designed_size() -> None:
    """windowed: this window must stay at its designed size, so maximize stays off."""
```

The suite must pass headless. Set `QT_QPA_PLATFORM=offscreen` to force that on any OS. On Linux with no `DISPLAY` and no `WAYLAND_DISPLAY`, the fixture selects offscreen for that test only and restores the variable afterward. Windows and macOS keep the native platform so a person can see the maximized window.

The maintained fixture is [conftest.py](conftest.py). It tries `PySide6`, `PyQt6`, `PySide2`, then `PyQt5`, and does nothing when none of them import. It does not construct `QApplication`; the test does, after the fixture has set the platform. Leftover top-level widgets are closed and deleted in teardown.

Extend that file. Do not add a second autouse patch of `show`.

Marker registration and the fixture (the body on disk is the one that runs):

```python
def pytest_configure(config: pytest.Config) -> None:
    """Register kit markers.

    config: pytest's config object. Each line is a marker name and its meaning.
    """
    config.addinivalue_line(
        "markers",
        "windowed: keep an exact window size; skip the default maximize-on-one-screen behavior",
    )


@pytest.fixture(autouse=True)
def maximize_top_level_windows(request, monkeypatch):
    """Show new top-level Qt windows maximized on one screen, then close them.

    request: this test. A windowed marker skips the maximize patch.
    monkeypatch: restores QT_QPA_PLATFORM and QWidget.show so they do not leak.
    """
```

Screen choice and the headless decision are pure functions in [window_policy.py](window_policy.py), covered by [unit/test_window_policy.py](unit/test_window_policy.py).

## Running

Use the **project's interpreter**: the virtualenv (or other env) that launches the app. Confirm before a run:

```bash
python -c "import sys; print(sys.executable)"
```

The printed path sits inside that environment. Create or activate it first (typical folder: `.venv`). From the repo root:

```bash
# macOS / Linux
.venv/bin/python -m pytest tests/unit -q
```

```powershell
# Windows PowerShell
.\.venv\Scripts\python.exe -m pytest tests/unit -q
```

Headless GUI tests on any OS:

```bash
QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest tests/unit -q
```

```powershell
$env:QT_QPA_PLATFORM = "offscreen"
.\.venv\Scripts\python.exe -m pytest tests/unit -q
```

Agents give the human that full command. The human pastes back the **final pytest summary line** (`5 passed in 0.04s`). A crash has no summary line; then paste the traceback.

One tier at a time, in run order. The chain that stops on the first failure is [Run order (fail-fast)](#run-order-fail-fast).

```bash
.venv/bin/python -m pytest tests/unit -q
.venv/bin/python -m pytest tests/smoke -q
.venv/bin/python -m pytest tests/integration -q
.venv/bin/python -m pytest tests/regression -q
```

```powershell
.\.venv\Scripts\python.exe -m pytest tests/unit -q
.\.venv\Scripts\python.exe -m pytest tests/smoke -q
.\.venv\Scripts\python.exe -m pytest tests/integration -q
.\.venv\Scripts\python.exe -m pytest tests/regression -q
```

## Comments

Every fixture and every helper documents **each input** in its docstring: arguments, fixture parameters, and environment variables it reads. One line per input, naming what the value is. This is the same rule as Coding_Standards for major functions, applied to test code. The kit's own copy of that shape is [unit/test_window_policy.py](unit/test_window_policy.py).

## Example unit test

Copy this shape. The function under test lives in the application; the test names the behavior and each input.

```python
def format_count(count: int) -> str:
    """Turn a count into a short label.

    count: how many items. Zero has its own label.
    """
    if count == 0:
        return "none"
    return str(count)


def test_format_count_names_zero() -> None:
    """count: zero items. The label is the word none."""
    assert format_count(0) == "none"
```

Bug fix: write the assertion you want, watch it fail, then change the function.

```python
def test_format_count_names_zero() -> None:
    """count: zero. Reproduces the bug that returned '0' instead of 'none'."""
    assert format_count(0) == "none"
```

Characterization, when the code already behaves and has no test: assert today's result, then edit.

## Capture on adoption

Generate **one** capture script as part of the smoke tier. One command runs it. Output goes to a gitignored folder. `CAPTURE_OUTPUT_DIR` and `CAPTURE_TEXT_DIR` override the defaults (see `.env.example`). Both keys accept a repo-relative path or an absolute path.

| App | Script to bind | What one command writes |
|-----|----------------|-------------------------|
| GUI (Qt or similar) | [scripts/capture_changelog_tabs.py](../scripts/capture_changelog_tabs.py) | PNG of the main window and each tab. Use the offscreen platform when there is no display. |
| Console, TUI, or other character UI | [scripts/capture_console_text.py](../scripts/capture_console_text.py) | Text files of stdout and stderr for the program, or for each main screen and command. |

Defaults (repo-relative, already gitignored):

| Kind | Env key | Default |
|------|---------|---------|
| GUI PNG | `CAPTURE_OUTPUT_DIR` | `data/Graphics/Screenshots/` |
| Console text | `CAPTURE_TEXT_DIR` | `data/ConsoleCaptures/` |

Until an app binds them, both scripts print the folder they would use and exit 2.

```bash
.venv/bin/python scripts/capture_changelog_tabs.py
.venv/bin/python scripts/capture_console_text.py -- python -m your_app --help
```

```powershell
.\.venv\Scripts\python.exe scripts\capture_changelog_tabs.py
.\.venv\Scripts\python.exe scripts\capture_console_text.py -- python -m your_app --help
```

**How this ties to Change_Log screenshots.** The capture writes raw files for review and diff. Those files stay gitignored. A Change_Log thumb is a second, curated step and only for a GUI view that actually changed:

```bash
.venv/bin/python scripts/promote_changelog_shot.py --tab main --source "data/Graphics/Screenshots/<file>.png"
```

`promote_changelog_shot.py` resizes that one PNG into `docs/changelog_shots/` and prints the **Shot:** line. PROCESS § Screenshots. Console captures have no thumbnail step; keep the text files locally and diff them.

Sketch once the GUI script is bound (your toolkit's grab; headless uses the offscreen platform):

```python
def grab(window, dest: Path) -> None:
    """Save one window to a PNG after paint is real.

    window: the top-level widget. Headless runs use the offscreen platform.
    dest: file path under the gitignored capture directory.
    """
    window.grab().save(str(dest), "PNG")
```

Sketch once the console script is bound. `command` is the list from `command_after_double_dash` (tokens after `--`). `folder` is `text_capture_dir(root, environ)`.

```python
def save_console(command: list[str], folder: Path) -> Path:
    """Run command and store stdout and stderr for review.

    command: program and arguments. folder: gitignored text-capture directory.
    """
    folder.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    dest = folder / "console.txt"
    dest.write_text(completed.stdout + completed.stderr, encoding="utf-8")
    return dest
```

## CI / pytest unfold (dormant)

This kit does **not** ship GitHub Actions or pytest-testmon. Keep it that way until PROCESS § **CI / pytest unfold**.

When the app crosses the threshold (≥25 unit tests, a suite runner, or the human asks for CI), the agent offers **one** purple pick. Recommended: unfold the Stock_Data shape — canaries first within unit, then smoke, integration, regression; testmon `--impacted` **locally**; CI runs that same order with **no** `--impacted`.
