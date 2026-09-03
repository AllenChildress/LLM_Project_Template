# Agent instructions — project template (staff kit)

Portable entry point. **Copy into each app** and replace the architecture paragraph.

## Architecture (one paragraph)

**YOUR_APP** is a … (fill: stack, data stores, UI shell). Prefer **named domain/session objects** over parallel `dict` caches for live state. Persistence is … (DB-first / files). Local runtime only: … (gitignore list).

## Context loading (mandatory)

**Never load the entire documentation set.** Open only:

1. Files listed in the **active** nested `AGENTS.md` for the directory you are editing, and/or  
2. Docs named in a **spawned subagent’s** instructions.

## Start here (on demand)

| When | Open |
|------|------|
| Process / commits | [docs/PROCESS.md](docs/PROCESS.md) |
| Style / errors / size | [docs/Coding_Standards.md](docs/Coding_Standards.md) |
| Backlog | [docs/ToDo.md](docs/ToDo.md) |
| Surprises | [docs/Lessons_Learned.md](docs/Lessons_Learned.md) |
| Vocabulary | [docs/Glossary.md](docs/Glossary.md) |
| Kit spine | [Project.md](Project.md) |
| Setup / install | [README.md](README.md) (Environment setup) |

Run `git status` and `git worktree list` before editing. Stage **only** this session’s files. Never `git add -A`.

## Parallel Session Rules (mandatory)

- **NEVER** edit the main working tree when any other Grok session is active.
- Every concurrent or long-running task **MUST** start in a dedicated git worktree + unique branch.
- **VS Code Grok Build (no launch switches):** before the first edit, confirm the worktree with a **purple multi-pick** — same shape as the old branch pick. Recommended **`New worktree wip/<short-topic>`** from the first message goes **first**, marked **`(Recommended)`**. Include **Stay in this tree**. The tool already adds **Other**.
- **CLI / TUI (optional):** `grok --worktree=<short-descriptive-name> --ref main "..."` — skip the pick when this session already lives in that worktree.
- Subagents that touch files: always request `isolation: worktree`. (`cwd` cannot combine with that — put the nested `AGENTS.md` working set in the spawn prompt.)
- Commit early and often on the worktree branch. Do not leave uncommitted changes that another session could see.
- Never assume shared state, open files, or previous multi-select answers from another session.
- **Database changes are single-threaded.** Worktrees share one database when they copy the same `.env`. Before DDL, migrations, or store schema work: `git worktree list`. This session must be the **only topic worktree** (primary checkout on `main` may remain). If another worktree is in play, **stop** and tell the human. Do not migrate while another session can use the database.
- When finished: push the branch, open a PR (or merge), then remove the worktree.
- Purple multi-picks **must not time out**: CLI `[toolset.ask_user_question] timeout_enabled = false`; VS Code `grok.acp.promptIdleTimeoutMs = 0`. If a pick **still** times out (old session / host bug): abort; do not continue in the same tree.

**Resume:** already in this session’s worktree and the first message is a continuation → stay (no pick).

Full write-up: [docs/PROCESS.md](docs/PROCESS.md) § Parallel sessions.

## Global coding standards (short)

- Type hints on public functions; explicit imports.
- Centralize errors; redact secrets in logs.
- Rule of Three before extracting shared helpers.
- Prefer domain/session objects over new parallel maps.
- **Multi-line SQL in `.sql` files** (DBA/schema lane owns text); app code loads/runs — see Coding_Standards.
- Tests under `tests/{unit,integration,smoke}/`. **CI/CD stays dormant** until PROCESS § CI / pytest unfold (then one purple pick — do not scaffold GitHub Actions or pytest-testmon on day one).
- Docs hygiene with the code: Change_Log / ToDo / Lessons when PROCESS requires it.
- Commits: clear subject; optional trailers `Assisted-by: Grok Build`.

## Orchestration (optional multi-agent)

Main session = orchestrator. Spawn specialists only for **large exclusive** work. File-touching children: `isolation: worktree`.

| Prompt mainly about… | Spawn (example) |
|----------------------|-----------------|
| Schema / SQL | `dba` |
| UI / presentation | `ui` |
| Tests | `tester` |
| Domain meaning | `domain` |
| External API | `integration` |
| Secrets | `security` |
| Docs only | `docs` |
| Tiny fix / chat judgment | **main only** |

See [docs/skills/General/Multi_Agent_Project_Setup.md](docs/skills/General/Multi_Agent_Project_Setup.md) if present.

## Agent identity

First line of each user-visible reply: `main:` or specialist name (`ui:`, `dba:`, …).

## Always-on checklist

| Question | Action |
|----------|--------|
| **New / concurrent / long-running session?** | Dedicated worktree + unique branch. **VS Code:** purple worktree pick before the first edit (Recommended `New worktree wip/<topic>` + Stay in this tree). **NEVER** edit the main working tree while another Grok session is active. File-touching subagents: `isolation: worktree`. |
| User-visible change? | Change_Log row (Why / What / Benefit) |
| User-visible **view paint**? | Run the app, screenshot each modified view, `python scripts/promote_changelog_shot.py`, add **Shot:** — PROCESS § Screenshots |
| Click-path tutorial (`docs/tutorial/`)? | Same series as UI or backend-that-affects-UI: update the matching tutorial page (PROCESS § Screenshots) |
| Backlog item? | Update ToDo |
| New API / persistence / UI flow? | Test under `tests/` |
| Testing past the kit stub? | If ≥25 unit tests, a suite runner, or the human asked for CI → **one** purple pick to unfold Stock_Data-style pytest (PROCESS § CI / pytest unfold). Do not unfold silently. |
| New / changed application code? | Cyclomatic complexity on touched functions — **CC ≤ 10** target, **CC > 15 too high** (PROCESS § Cyclomatic complexity) |
| Non-obvious fix? | Lessons_Learned |
| Database / schema change? | Single-threaded: `git worktree list` — this session must be the only topic worktree, then migrate. |
| Secrets? | Never commit |

## Do not commit

`.env`, tokens, dumps, local override configs, large binaries unless intentional.
