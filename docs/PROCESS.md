# Process (portable)

How humans and agents work on **any** project that uses this staff kit.

## Principles

1. **Outcome-level work** — design, implement, smoke, document without re-teaching process each time.
2. **Docs with the code** — same change series as behavior.
3. **When a session finishes:** `git switch main && git pull --ff-only`. If the diff is worth keeping, branch off that `main`, commit, squash-merge, delete the local branch and the remote branch. Then `grok worktree rm <id>` if this session used a managed worktree. Do not delete the primary checkout.
4. **Short answers** to humans; completeness is in files and tests, not essay chat.

## Change_Log

For user-visible behavior: add a row with **Why** / **What** / **Benefit**.  
Prefer a vertical list (heading + bullets) if wide tables break your preview tool.

### Screenshots (each push that paints a view)

Goal: a visible **progression** of the UI, not a dump of error captures.

**When required:** the change altered what a user sees (window, tab, pane, chrome). Docs-only, schema-only, and headless work skip this.

**Same series as the code:**

1. Run the app (or a smoke shell if chrome-only).
2. Open **each modified view**. Wait until paint is real — not a spinner or blank pane.
3. Capture the window. Raw dumps go to a **gitignored** folder (typical: `data/Graphics/Screenshots/`).
4. Promote a tracked JPEG thumb:
   ```powershell
   python scripts/promote_changelog_shot.py --tab main --source "data/Graphics/Screenshots/<file>.png"
   ```
   Replace `--tab` slugs with your app’s views (`main`, `settings`, `log`, `shell`, …).
5. Paste the printed `- **Shot:** <img …>` line on that Change_Log entry. Add the thumb to the **UI progression** strip at the top of Change_Log when it is a real step (new view, new overlay, new layout).
6. **Do not** promote `error_*` / `*_fail_*` dumps. Those stay local diagnostics.
7. Views that show **PII, account numbers, or money** need `--allow-sensitive` (privacy mode or crop first). Prefer non-sensitive views for the public strip.

Thumbs live in `docs/changelog_shots/` (tracked, JPEG, max width 900). Runtime PNGs stay gitignored.

If the app keeps a **click-path tutorial** (`docs/tutorial/`), update the matching page in the **same series** as a UI change or a backend change that alters what the user clicks or sees. Skip when there is no user-visible click/paint change. Keep those pages short (click → see → one thumb), not a second feature list.

Apps with a desktop shell should also keep a `scripts/capture_changelog_tabs.py` that boots the UI, waits for paint, and grabs each requested tab. The copy in this kit is a **stub** — bind it to your window.

## ToDo

- Open work in backlog columns.
- Finished items → **Done ✓** (or remove from open and record in Change_Log if user-visible).
- Do not leave stale checked items in “open” forever.

## Lessons_Learned

Non-obvious fixes, environmental traps, “never do X again.” Prefer durable rules over novel-length narratives.

## Commits

- Clear subject (what/why in one line).
- Optional body for multi-file stories.
- Optional trailer: `Assisted-by: Grok Build` (or your tool name).
- PowerShell-safe: write message to a file, `git commit -F …` (avoid nested quotes).

## Tests

| Tier | When |
|------|------|
| **unit** | Pure logic, fast, no live network |
| **integration** | Cross-module, may use local DB/services |
| **smoke** | Shell boots, critical path “still alive” |

New behavior → at least unit unless the only risk is shell-level.

### CI / pytest unfold (dormant until a threshold)

**Default is dormant.** A new app gets `tests/{unit,integration,smoke}/` and `python -m pytest tests/unit -q`. It does **not** get GitHub Actions, `pytest-testmon`, or a canary harness on day one. Do not copy Stock_Data’s `src/testing/` or `.github/workflows/` until the human says yes.

**Threshold — unfold is due when any one is true**

| Signal | Why it is enough |
|--------|------------------|
| **≥ 25** collected unit tests (not kit stubs) | “Run everything” starts to hide failures |
| A `scripts/testing/` suite runner exists | Tiers are already a product |
| The human asks for CI / GitHub Actions | They named the need |

**Then one purple pick** (Recommended first, **Decide later** on the same card). Do **not** unfold silently. Do **not** re-ask every session — write the answer in ToDo.

| Pick | Agent does |
|------|------------|
| **Unfold Stock_Data-style pytest (Recommended)** | Canaries first, then unit. Local `--impacted` via **pytest-testmon**. GitHub Actions: canaries then unit, **no** `--impacted` on CI (clean runner has no testmon map). Gitignore `.testmondata`. OOP `TestLane` list, not a tier-string switch. Reference: Stock_Data `src/testing/` + `scripts/testing/run_smoke_suite.py` + `.github/workflows/unit-tests.yml`. |
| **Stay dormant** | Keep pytest local only. Record the skip in ToDo. |
| **Decide later** | Same as Stay dormant until they pick again. |

**Unfold shape (when they choose Recommended)**

1. `tests/{unit,integration,smoke}/` — cases stay `test_*` functions unless the app already uses classes.
2. `canaries.json` — a short sniff list (typical moles) that runs **before** the rest of unit.
3. Suite script under `scripts/testing/` with `--tier` and optional `--impacted`.
4. `pytest-testmon` in requirements; `.testmondata` gitignored; `--impacted` is **local only**.
5. `.github/workflows/` unit job: `windows-latest` (or the app’s OS), pip + `requirements.txt` (not a private conda env), canaries then unit.

Until that pick, agents: no workflow YAML, no testmon dependency, no canary package.

### Cyclomatic complexity (new / changed code)

When a slice of application code is done, score **touched functions** (McCabe). Stock_Data: `python scripts/score_cc.py <files>` (same visitor as the Tech Debt tab).

| | Gate |
|--|------|
| **Target** | CC **≤ 10** |
| **Too high** | CC **> 15** — split or a named leave-whole note |

Uncle Bob (Matt Pocock 2026-08-19) ran a **Complexity Score** (complexity × coverage) first on agent output — human **< 4**, agents **6–8**. A Tech Debt / hotspot table (CC × churn) is the cousin you can ship before coverage is in the loop. Do not invent a second formula.

## Migrations / schema (if DB included)

- Versioned SQL or migration tool of choice.
- Document apply order in a short runbook.
- Backup before destructive migrations.
- **SQL text lives in files** (Coding_Standards § SQL lives in files): queries and DDL are `.sql` (or migration files), not string literals in app code. App code loads and runs that text.
- Same change series: delta/migration + embedded/schema SQL the app applies + docs (Schema / runbook) when the live schema moves.

## Parallel sessions (mandatory)

Requires Grok Build 1.0.42 or newer.
1.0.5 reclaims idle checkouts under `~/.grok/worktrees` when safe and never deletes the last copy.
1.0.19 adds `--worktree` to headless `grok -p`.
1.0.42 adds `grok worktree create` (managed worktree, no session).
A Grok worktree is a detached checkout at the base commit. It does not create a branch. Ending a session does not remove it. Land with ordinary git. Remove with `grok worktree rm` or `grok worktree gc --max-age 7d`.

Git workflow detail: read [`.grok/skills/git-workflow-and-versioning/SKILL.md`](../.grok/skills/git-workflow-and-versioning/SKILL.md).
Second-writer worktree rules and branch-delete rules in this file override that skill.
Skill owns commit shape, message style, and PR detail. This file owns when a worktree exists and that the branch dies with the merge.

**Lock:** two chats in one folder share one checkout. A Grok worktree is a **detached** checkout at the base commit. It is not `git worktree add -b wip/<topic>`. Never edit the primary checkout while another Grok session is editing.

### Start

- **One writer, short task:** stay in the primary checkout. No worktree. No branch until the diff is worth keeping.
- **Second writer, or a task long enough that another writer may start:** Grok managed worktree, detached, off current `main`.
  - **CLI:** `grok -w --ref main`
  - **No session yet:** `grok worktree create`
  - **VS Code:** purple pick, **recommended only in this case**. Label it as a detached Grok worktree. Do not use `git worktree add -b wip/<topic>`.
- **Subagents that edit files:** `isolation: worktree`. Read-only children need no worktree.
- If this session is **already** in its worktree and the first message is a continuation → stay. No pick.
- Stage **only** this session’s files. Never `git add -A`.

**VS Code Grok Build** — purple multi-pick **only** when a second writer (or a long task) needs a worktree. Recommended first, marked **`(Recommended)`**:

| Human picks | Agent does |
|-------------|------------|
| **Detached Grok worktree (Recommended)** | Use a Grok managed worktree off current `main` (`grok -w --ref main` / `grok worktree create`). Tell them the folder path. **Do not** run `git worktree add -b wip/<topic>`. **Do not keep editing the primary tree.** |
| **Stay in this tree** | Stay only for one writer, short task, in the primary checkout, with no other Grok session editing. If this is the primary tree and another Grok session is editing → **stop**. Do not `checkout -b` here to “make room.” |
| **Other** | Name they typed: same create path as Detached Grok worktree. |

### During

- Do not leave uncommitted changes that another session could see in a shared checkout.
- Never assume shared state, open files, or previous multi-select answers from another session.

### Database (single-threaded)

Worktrees copy `.env`, so they all talk to the **same** database. Schema, migrations, and store DDL are **not** isolated.

Before any database change (migrations, schema SQL, destructive store work):

1. Run `git worktree list`.
2. This session must be the **only topic worktree**. The primary checkout on `main` may remain. A second topic worktree means **stop**.
3. Tell the human. Do not migrate while another session can run the app or apply its own DDL against that database.

Idle leftover folders still count until they are removed. Isolating databases per worktree is later work; until then this gate is the fence.

### Purple multi-picks (do not time out)

The human answers purple cards when ready. They **must not** expire.

| Layer | Lock |
|-------|------|
| Grok CLI / TUI | `~/.grok/config.toml` **and** `~/.grok/requirements.toml`: `[toolset.ask_user_question] timeout_enabled = false`. Do not turn **Ask-Question timeout** on in `/settings`. |
| VS Code Grok Build | `grok.acp.promptIdleTimeoutMs = 0` (User settings **and** the workspace). `0` disables the 30-minute idle cap. Applies to **new** sessions. |

### Abort

If a permission / multi-select **still times out** (old session started before the lock, or a host bug): treat the session as aborted. Do not continue in the same tree.

### Wrap-up

When finished:

1. `git switch main && git pull --ff-only`.
2. If the diff is worth keeping: branch off that `main`, commit (stage only this session’s files), squash-merge, delete the local branch and the remote branch. A detached worktree that dies is a folder, not a branch.
3. After merge: `grok worktree rm <id>` if this session used a managed worktree. Do not delete the primary checkout.
4. Finish pass: `grok worktree list`, `git worktree list`, `git branch -vv`. A branch with no worktree and no open PR is trash. Idle worktrees count until removed.
5. Last line: `Push Complete` when the PR is open or landed. Use `Done` only when work is finished locally and **not** pushed (abort / hold).

### Wrong base (no unique commits)

```text
git stash push -u -m "wip notes"
git reset --hard main
git stash pop
```

If the checkout has unique commits to keep: `git rebase main` in that folder (not reset). A detached worktree that dies is a folder, not a branch.

Agent checklist: root [AGENTS.md](../AGENTS.md) § Parallel Session Rules.

## Handoff to human

Short: what changed · files · how to verify · docs · branch landed and deleted · worktree removed if any.

## Solo / small team (keep light)

See [Project.md](../Project.md) § Lightweight practices. In short: shippable main, read your own diff, lock dependencies, update ToDo/Change_Log with the code.
