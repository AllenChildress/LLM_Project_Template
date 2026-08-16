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

## New chat session → own branch **and** own folder

A **new Grok/chat session** (the human opened a new conversation) owns a **topic branch** **and** a **sibling folder** (git worktree). A branch name alone is **not** isolation — one folder can only have one branch checked out. **Subagents do not get a branch or a folder** — they stay on this session’s branch and tree.

**Before the first edit** in a new session, if HEAD is `main` / `master` or another session’s `wip/*`:

1. Run `git status`, `git branch --show-current`, and `git worktree list`. If this folder already has uncommitted files this session did not write, **say so** — do not carry someone else’s WIP.
2. Confirm the **branch name** with a **purple multi-pick**. Recommended `wip/<short-topic>` from the first message goes **first**, marked **`(Recommended)`**. Include **Stay on current branch**. The tool already adds **Other**.
3. Confirm **where** with a second purple pick (same turn is fine):
   - **New sibling folder (Recommended)** — isolated worktree + new branch.
   - **This folder** — `checkout -b` here. **Loud warning:** every other chat using this folder is now on that branch; their uncommitted files come along.
   - **Stay on current branch** — no checkout, no worktree.
4. After **New sibling folder**:  
   `git worktree add "<parent>\<RepoName>_<topic>" -b wip/<topic> main`  
   Example: this repo is `C:\Users\You\Projects\MyApp` → `C:\Users\You\Projects\MyApp_privacy-mode`.  
   **Always pass `main`** (or another explicit start commit). Omit it and the new branch starts at this folder’s HEAD.  
   Then **stop and tell the human** (do not keep editing here): open a **new** Grok chat **in that folder**. This chat stays in the original folder. Do not `checkout` this folder onto the new branch.
5. After **This folder**: `git checkout -b wip/<name>` and warn again. Do not push until asked.
6. Stage **only** this session’s files. Never `git add -A`.

**Resume:** already on `wip/<topic>` in the folder this chat opened, and the first message is a continuation → stay. Do not invent a second branch or a second folder.

**Wrap-up:** pushing does not move any folder. If you used **This folder**, `git checkout main` when the session finishes. If you used a sibling, leave the primary folder on `main` and `git worktree remove` the sibling after they are done with it. Merge only when asked.

Full write-up: [docs/PROCESS.md](docs/PROCESS.md) § New Grok session → branch + folder.

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
| **New chat session on `main`?** | Multi-pick `wip/<topic>` **and** a sibling folder (worktree **from `main`**) **before edits**. `checkout -b` in this folder is the exception. After a **This folder** session, `git checkout main`. Subagents do not branch. |
| User-visible change? | Change_Log row (Why / What / Benefit) |
| User-visible **view paint**? | Run the app, screenshot each modified view, `python scripts/promote_changelog_shot.py`, add **Shot:** — PROCESS § Screenshots |
| Backlog item? | Update ToDo |
| New API / persistence / UI flow? | Test under `tests/` |
| Non-obvious fix? | Lessons_Learned |
| Secrets? | Never commit |

## Do not commit

`.env`, tokens, dumps, local override configs, large binaries unless intentional.
