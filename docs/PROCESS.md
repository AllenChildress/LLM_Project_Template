# Process (portable)

How humans and agents work on **any** project that uses this staff kit.

## Principles

1. **Outcome-level work** — design, implement, smoke, document without re-teaching process each time.
2. **Docs with the code** — same change series as behavior.
3. **Do not push** until the human has tested (or explicitly waived) and asked to push.
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

## New Grok session → branch (one folder)

**Default: one project folder.** Do **not** `git worktree add` unless the human explicitly asks. Extra checkouts (missing `.env` / tokens / caches, two chats, rebase soup) were worse than sharing one checkout.

Git can check out only **one** branch in a given folder. Two chats there share that checkout. Prefer one editing session at a time, or **Stay on current branch**.

**Default (agents):** after they pick `wip/<topic>`:

```text
git checkout -b wip/<topic>
```

Warn if other uncommitted WIP would come along. Subagents never create a branch.

### Wrap-up

Pushing does **not** change the checkout. After `Done` / `Push Complete`: `git checkout main` so the next chat here is not still on `wip/<topic>`.

### Wrong base (no unique commits)

```text
git stash push -u -m "wip notes"
git reset --hard main
git stash pop
```

If the sibling has unique commits to keep: `git rebase main` in that folder (not reset).

Agent checklist: root [AGENTS.md](../AGENTS.md) § New chat session → own branch and folder.

## Handoff to human

Short: what changed · files · how to verify · docs · push status (local until asked).

## Solo / small team (keep light)

See [Project.md](../Project.md) § Lightweight practices. In short: shippable main, read your own diff, lock dependencies, update ToDo/Change_Log with the code, multi-agent only when the work tree is large and exclusive.
