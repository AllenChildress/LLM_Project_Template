# Tests

```text
tests/
  unit/           # fast, isolated
  integration/    # cross-module / local services
  smoke/          # boot + critical path
```

## Conventions

- Prefer unit tests for new logic.
- Integration when contracts cross packages or need a real local DB.
- Smoke when “does the app still start / critical UI path work?” matters.
- Keep secrets out of fixtures; use env or local-only config.

## Running (example)

```powershell
# Adjust to your runner
python -m pytest tests/unit -q
```

Add a thin suite script under `scripts/testing/` when the app grows.

## CI / pytest unfold (dormant)

This kit does **not** ship GitHub Actions or pytest-testmon. Keep it that way until PROCESS § **CI / pytest unfold**.

When the app crosses the threshold (≥25 unit tests, a suite runner, or the human asks for CI), the agent offers **one** purple pick. Recommended: unfold the Stock_Data shape — canaries first, then unit; testmon `--impacted` **locally**; CI runs canaries then unit with **no** `--impacted`.
