# Glossary (portable starter)

Shared vocabulary for humans and agents. **Add product terms here** as the app grows.

| Term | Meaning |
|------|---------|
| **Staff kit** | Portable process pack: AGENTS, PROCESS, Coding_Standards, Change_Log/ToDo/Lessons norms, test layout — first-class in git, updated with code. |
| **cache_key** | Structured identity for a data slice (e.g. tuple of entity / range / version). Not a UI page string. |
| **page_key** | Path-safe string identity for a UI page/document/slot (if the app has one). Prefer over vague “slug” for view caches. |
| **Mixin** | Small class that contributes one behavior slice via composition/inheritance — not a god window. |
| **Smoke test** | Minimal “system still boots / critical path alive” check. |
| **Unit test** | Fast, isolated logic test. |
| **Integration test** | Cross-module; may use local services. |
| **Change_Log** | User-visible history (Why / What / Benefit). |
| **ToDo** | Backlog; finished work leaves open columns. |
| **Worktree** | A second **folder** of the same git repo, each with its own checked-out branch. Concurrent Grok sessions **must** use one. **VS Code:** purple-pick before the first edit, then `git worktree add PATH -b wip/<topic> main`. **CLI/TUI:** `grok --worktree=<name> --ref main`. Always pass **`main`**. |
| **Done** | Last line of a finished Grok session that was **not** pushed (abort / hold). |
| **Push Complete** | Last line of a finished Grok session after the topic branch was pushed, a PR opened (or merged), and the worktree removed. |

## Libraries (common Python)

| Library | Role |
|---------|------|
| **pytest** | Test runner |
| **python-dotenv** | Load `.env` into process env |
| **psycopg** | PostgreSQL driver (v3) |
| **pandas** | DataFrames / tabular analysis |
| **numpy** | Arrays / numeric core under pandas |
| **PyQt6** | Desktop UI (if desktop app) |
| **requests** / **httpx** | HTTP clients |
| **pydantic** | Validated models / settings |

See [Libraries.md](Libraries.md) for a fuller menu and [Database.md](Database.md) for Postgres vs SQLite vs Timescale.

Delete unused rows; never leave secrets or personal data here.
