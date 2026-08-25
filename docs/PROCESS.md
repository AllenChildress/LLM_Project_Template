# Process (portable)

How humans and agents work on **any** project that uses this staff kit.

## Principles

1. **Outcome-level work** — design, implement, smoke, document without re-teaching process each time.
2. **Docs with the code** — same change series as behavior.
3. **When a session finishes:** push the topic branch, open a PR (or merge if the human asked to merge), then remove the worktree. Pushing a topic branch is not a merge to `main`.
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

## Migrations / schema (if DB included)

- Versioned SQL or migration tool of choice.
- Document apply order in a short runbook.
- Backup before destructive migrations.
- **SQL text lives in files** (Coding_Standards § SQL lives in files): multi-line queries and DDL are `.sql` (or migration files), not string literals in app code. The DBA / database lane owns the statement text; app code loads and runs it.
- Same change series: delta/migration + embedded/schema SQL the app applies + docs (Schema / runbook) when the live schema moves.

## Parallel sessions (mandatory)

**Lock:** parallel Grok sessions use **isolated git worktrees**, not a shared primary checkout. A branch name is not isolation — two chats in one folder share one checkout. `checkout -b` in the second chat **moves** the first and mixes uncommitted files.

### Start

- **NEVER** edit the main working tree when any other Grok session is active.
- Every **concurrent** or **long-running** task **MUST** start in a dedicated git worktree + unique branch.
- If this session is **already** in its worktree and the first message is a continuation → stay. No pick.
- Subagents that **touch files**: always `isolation: worktree`. Read-only children may pass module `cwd`. `cwd` and worktree isolation are mutually exclusive; when isolated, paste the nested `AGENTS.md` working set into the spawn prompt.
- Stage **only** this session’s files. Never `git add -A`.

**VS Code Grok Build** has no `--worktree` launch switch. **Before the first edit**, if this session is in the primary tree (or another session’s worktree), confirm with a **purple multi-pick** — same shape as the old branch pick:

| Human picks | Agent does |
|-------------|------------|
| **`New worktree wip/<short-topic>` (Recommended)** | `git worktree add "<parent>\<RepoName>_<topic>" -b wip/<topic> main` (always pass **`main`**). Copy gitignored runtime (`.env`, tokens, caches) from the primary checkout. Tell them the folder path. **Do not keep editing the primary tree** — they continue by opening that folder in VS Code (or a new Grok chat there). |
| **Stay in this tree** | Stay only if this is already the session’s worktree. If this is the primary tree and another Grok session is active → **stop**. Do not `checkout -b` here to “make room.” |
| **Other** | Name they typed: same create path as New worktree. |

**CLI / TUI (optional):** when they can pass flags, `grok --worktree=<short-descriptive-name> --ref main "<prompt>"` already lives in the worktree — skip the pick. Use `--worktree=` (with `=`) so the prompt is not swallowed as the label.

### During

- Commit **early and often** on the worktree branch. Do not leave uncommitted changes that another session could see.
- Never assume shared state, open files, or previous multi-select answers from another session.

### Abort

If a permission / multi-select **times out**: treat the session as aborted. Do not continue in the same tree.

### Wrap-up

When finished:

1. Commit remaining work on the worktree branch.
2. **Push** the branch.
3. Open a **PR** (or **merge** if the human asked to merge). Pushing a topic branch is not a merge to `main`.
4. **Remove** the worktree (`git worktree remove <path>` or `grok worktree rm`). Never delete the primary checkout.
5. Last line: `Push Complete`. Use `Done` only when work is finished locally and **not** pushed (abort / hold).

### Wrong base (no unique commits)

```text
git stash push -u -m "wip notes"
git reset --hard main
git stash pop
```

If the worktree has unique commits to keep: `git rebase main` in that folder (not reset).

Agent checklist: root [AGENTS.md](../AGENTS.md) § Parallel Session Rules.

## Handoff to human

Short: what changed · files · how to verify · docs · branch pushed + PR (or merge) · worktree removed.

## Solo / small team (keep light)

See [Project.md](../Project.md) § Lightweight practices. In short: shippable main, read your own diff, lock dependencies, update ToDo/Change_Log with the code, multi-agent only when the work tree is large and exclusive.
