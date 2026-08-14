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

Run `git status` before editing. **Do not push** until the human explicitly asks.

## New chat session → own branch

A **new Grok/chat session** (the human opened a new conversation) owns a **topic branch**. **Subagents do not get a branch** — they stay on this session’s branch.

**Before the first edit** in a new session, if HEAD is `main` / `master` or another session’s `wip/*`:

1. Run `git status` and note the current branch. If the tree already has uncommitted files this session did not write, **say so** — `checkout -b` would carry that WIP onto the new branch.
2. Confirm the name with a **purple multi-pick** (`ask_user_question`). Recommended `wip/<short-topic>` from the first message goes **first**, marked **`(Recommended)`**. Include **Stay on current branch**. The tool already adds **Other** — that is how they type a custom name; do not omit the multi-pick.
3. After they pick: `git checkout -b wip/<name>` (or the name they typed / Other). Do not push until asked.
4. Stage **only** this session’s files. Never `git add -A`.

**Same folder, two chats:** one working tree cannot be on two branches at once. Prefer a second **worktree** (`git worktree add <folder> -b wip/<topic>`) and open the new session **in that folder**. If they stayed here, still create the branch after the pick — and warn if other WIP would come along.

**Resume:** already on `wip/<topic>` and the first message is a continuation → stay. Do not invent a second branch.

## Global coding standards (short)

- Type hints on public functions; explicit imports.
- Centralize errors; redact secrets in logs.
- Rule of Three before extracting shared helpers.
- Prefer domain/session objects over new parallel maps.
- **Multi-line SQL in `.sql` files** (DBA/schema lane owns text); app code loads/runs — see Coding_Standards.
- Tests under `tests/{unit,integration,smoke}/`.
- Docs hygiene with the code: Change_Log / ToDo / Lessons when PROCESS requires it.
- Commits: clear subject; optional trailers `Assisted-by: Grok Build`.

## Orchestration (optional multi-agent)

Main session = orchestrator. Spawn specialists only for **large exclusive** work.

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
| **New chat session on `main`?** | Multi-pick `wip/<topic>` **before edits** — see § New chat session → own branch. Subagents do not branch. |
| User-visible change? | Change_Log row (Why / What / Benefit) |
| User-visible **view paint**? | Run the app, screenshot each modified view, `python scripts/promote_changelog_shot.py`, add **Shot:** — PROCESS § Screenshots |
| Backlog item? | Update ToDo |
| New API / persistence / UI flow? | Test under `tests/` |
| Non-obvious fix? | Lessons_Learned |
| Secrets? | Never commit |

## Do not commit

`.env`, tokens, dumps, local override configs, large binaries unless intentional.
