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

## Global coding standards (short)

- Type hints on public functions; explicit imports.
- Centralize errors; redact secrets in logs.
- Rule of Three before extracting shared helpers.
- Prefer domain/session objects over new parallel maps.
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
| User-visible change? | Change_Log row (Why / What / Benefit) |
| Backlog item? | Update ToDo |
| New API / persistence / UI flow? | Test under `tests/` |
| Non-obvious fix? | Lessons_Learned |
| Secrets? | Never commit |

## Do not commit

`.env`, tokens, dumps, local override configs, large binaries unless intentional.
