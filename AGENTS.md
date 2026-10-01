# Agent instructions — project template (staff kit)

Portable entry point. **Copy into each app** and replace the architecture paragraph.

## Architecture (one paragraph)

**YOUR_APP** is a … (fill: stack, data stores, UI shell). Prefer **named domain/session objects** over parallel `dict` caches for live state. Persistence is … (DB-first / files). Local runtime only: … (gitignore list).

## Context loading (mandatory)

**Never load the entire documentation set.** Open only:

1. Files listed in the **active** nested `AGENTS.md` for the directory you are editing.
2. Docs the task names.

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

Requires Grok Build 1.0.42 or newer.
1.0.5 reclaims idle checkouts under `~/.grok/worktrees` when safe and never deletes the last copy.
1.0.19 adds `--worktree` to headless `grok -p`.
1.0.42 adds `grok worktree create` (managed worktree, no session).
A Grok worktree is a detached checkout at the base commit. It does not create a branch. Ending a session does not remove it. Land with ordinary git. Remove with `grok worktree rm` or `grok worktree gc --max-age 7d`.

Git workflow detail: read `.grok/skills/git-workflow-and-versioning/SKILL.md`.
Second-writer worktree rules and branch-delete rules in this file override that skill.
Skill owns commit shape, message style, and PR detail. This file owns when a worktree exists and that the branch dies with the merge.

- **One writer, short task:** stay in the primary checkout. No worktree. No branch until the diff is worth keeping.
- **Second writer, or a task long enough that another writer may start:** Grok managed worktree, detached, off current `main`.
  - **CLI:** `grok -w --ref main`
  - **No session yet:** `grok worktree create`
  - **VS Code:** purple pick, **recommended only in this case**. Label it as a detached Grok worktree. Do not use `git worktree add -b wip/<topic>`.
- **Subagents that edit files:** `isolation: worktree`. Read-only children need no worktree.
- **Never** edit the primary checkout while another Grok session is editing.
- Stage **only** this session’s files. Never `git add -A`.
- Do not leave uncommitted changes that another session could see in a shared checkout.
- Never assume shared state, open files, or previous multi-select answers from another session.
- **Database changes are single-threaded.** Worktrees share one database when they copy the same `.env`. Before DDL, migrations, or store schema work: `git worktree list`. This session must be the **only topic worktree** (primary checkout on `main` may remain). If another worktree is in play, **stop** and tell the human. Do not migrate while another session can use the database.
- Secrets: never commit `.env`, tokens, dumps, or local override configs.

**Land (both cases):** `git switch main && git pull --ff-only`. If the diff is worth keeping, branch off that `main`, commit, squash-merge, delete the local branch and the remote branch. A detached worktree that dies is a folder, not a branch.

**After merge:** `grok worktree rm <id>`. Do not delete the primary checkout.

**Finish pass:** `grok worktree list`, `git worktree list`, `git branch -vv`. A branch with no worktree and no open PR is trash. Idle worktrees count until removed.

**Resume:** already in this session’s worktree and the first message is a continuation → stay (no pick).

Purple multi-picks **must not time out**: CLI `[toolset.ask_user_question] timeout_enabled = false`; VS Code `grok.acp.promptIdleTimeoutMs = 0`. If a pick **still** times out (old session / host bug): abort; do not continue in the same tree.

Full write-up: [docs/PROCESS.md](docs/PROCESS.md) § Parallel sessions.

## Global coding standards (short)

- Type hints on public functions; explicit imports.
- Centralize errors; redact secrets in logs.
- Rule of Three before extracting shared helpers.
- Prefer domain/session objects over new parallel maps.
- **SQL lives in `.sql` files**; app code loads and runs it — see Coding_Standards.
- Tests under `tests/{unit,integration,smoke}/`. **CI/CD stays dormant** until PROCESS § CI / pytest unfold (then one purple pick — do not scaffold GitHub Actions or pytest-testmon on day one).
- Docs hygiene with the code: Change_Log / ToDo / Lessons when PROCESS requires it.
- Commits: clear subject; optional trailers `Assisted-by: Grok Build`.

## How this session works

This session does the work. Nested `AGENTS.md` files are extra reading lists for that folder. Replies start with the answer. No role label on the first line (`main:`, `dba:`, `ui:`, or any other).

## Always-on checklist

| Question | Action |
|----------|--------|
| **New / concurrent / long-running session?** | One writer, short task: primary checkout, no worktree, no branch until the diff is worth keeping. Second writer or a long task: Grok managed worktree (`grok -w --ref main` / `grok worktree create`). **VS Code:** purple pick **recommended only** for that second-writer case (detached Grok worktree). **Never** edit the primary checkout while another Grok session is editing. Requires Grok Build 1.0.42 or newer. |
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
