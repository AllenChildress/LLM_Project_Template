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

## Handoff to human

Short: what changed · files · how to verify · docs · push status (local until asked).
