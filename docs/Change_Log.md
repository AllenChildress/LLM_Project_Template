# Change Log

All notable changes to **YOUR_APP** are recorded here.

Each entry: **date**, optional time, **files**, short title, then **Why** / **What** / **Benefit**.

Prefer a **vertical list** (not a wide table) so Markdown Preview stays readable.

| Field | Role |
|-------|------|
| **Files** | Paths or short module names touched |
| **Why** | Problem or product need |
| **What** | What shipped (concrete) |
| **Benefit** | Short user/dev outcome |
| **Shot** | Required when a **view or chrome paint** changed — HTML thumbnail from [changelog_shots/](changelog_shots/) (see PROCESS § Screenshots) |

**Shot:** use the HTML thumbnail `scripts/promote_changelog_shot.py` prints (width 360). Do not embed full-size PNGs or error dumps.

### UI progression (curated)

Newest real UI steps, oldest last. Same image may also appear on the dated **Shot:** row — that is intentional.

<!-- Add promoted thumbs here, newest first. Example:
- YYYY-MM-DD Main window  
  <img src="changelog_shots/YYYY-MM-DD_main.jpg" width="360" alt="YYYY-MM-DD main">
-->

## Benefit vocabulary (optional)

- Bug fix  
- Save user time / workflow speed  
- Improve accuracy / data correctness  
- Performance increase  
- Reduce technical debt  
- Improve maintainability  
- UX clarity  
- Reliability / stability  
- Security  
- Tests / regression prevention  
- New feature  
- Improve code hygiene / documentation  

---

## Entries (newest first)

### 2026-09-03 — Purple multi-picks do not time out

- **Files:** `AGENTS.md`, `docs/PROCESS.md`
- **Why:** A timed-out pick looks declined and the agent keeps going in the wrong tree. The CLI default is 30 minutes; VS Code Grok Build also idles `session/prompt` at 30 minutes of silence.
- **What:** Lock CLI `[toolset.ask_user_question] timeout_enabled = false` (`~/.grok/config.toml` and `requirements.toml`). VS Code: `grok.acp.promptIdleTimeoutMs = 0`. Abort only if a pick **still** times out (old session / host bug).
- **Benefit:** Reliability / stability

### 2026-08-25 — Database changes are single-threaded across worktrees

- **Files:** `AGENTS.md`, `docs/PROCESS.md`, Lessons
- **Why:** Worktrees copy `.env`, so they share one database. Two sessions migrating, or one migrating while another runs the app, will collide.
- **What:** Before DDL / migrations, `git worktree list`. This session must be the **only topic worktree** (primary `main` checkout may remain). If another worktree is in play, stop and tell the human.
- **Benefit:** Reliability / stability

### 2026-08-25 — Parallel Grok sessions: worktree isolation

- **Files:** `AGENTS.md`, `docs/PROCESS.md`, Glossary, Lessons, `docs/Coding_Standards.md`
- **Why:** Two Grok chats in the primary folder share one checkout. `checkout -b` in the second chat moves the first and mixes uncommitted files. VS Code Grok Build has no `--worktree` launch switch.
- **What:** Concurrent / long-running sessions **must** start in a dedicated worktree + unique branch. **VS Code:** purple worktree pick before the first edit (Recommended `New worktree wip/<topic>` + Stay in this tree); create from `main`, copy locals, stop editing the primary tree. **CLI/TUI:** `grok --worktree=<name> --ref main`. File-touching subagents: `isolation: worktree`. Finish: push + PR (or merge) + remove the worktree. Permission timeout aborts the tree. The 2026-08-17 one-folder lock is reversed.
- **Benefit:** Reliability / stability

### 2026-08-20 — Table columns autosize then stay resizable

- **Files:** `docs/Coding_Standards.md`
- **Why:** Desktop tables that lock column widths fight the mouse.
- **What:** UI standard: autosize columns to contents on first paint, then leave them user-resizable. Stretch at most the last column. Icon/checkbox columns may stay fixed.
- **Benefit:** UX clarity

### 2026-08-16 — Session wrap-up returns the shared folder to main

- **Files:** `AGENTS.md`, `docs/PROCESS.md`, `docs/Lessons_Learned.md`, `docs/Glossary.md`
- **Why:** `git worktree add` without a start-point inherits this folder’s HEAD. Pushing a topic branch does not move any folder back to `main`.
- **What:** Always pass `main` to `worktree add`. After a **This folder** session, `git checkout main` (checkout ≠ merge). PROCESS wrap-up table.
- **Benefit:** Improve code hygiene / documentation

### 2026-08-17 — One folder; no default worktrees

- **Files:** `docs/PROCESS.md`, `docs/Lessons_Learned.md`
- **Why:** Sibling worktrees made a mess. Human lock: stay in the project folder.
- **What:** New session = `checkout -b` here. `git worktree add` only if asked.
- **Benefit:** Improve code hygiene / documentation

### 2026-08-15 — Lessons: Grok multi-session

- **Files:** `docs/Lessons_Learned.md`
- **Why:** A “harmless” second chat that only `checkout -b` in the same folder can mix WIP and block a push. Two chats also cannot DM each other.
- **What:** New **Grok multi-session** category: branch ≠ folder, no inter-session backchannel, sibling worktree then open the chat there, `git worktree remove` when done.
- **Benefit:** Improve code hygiene / documentation

### 2026-08-15 — New session = branch + sibling folder

- **Files:** `AGENTS.md`, `docs/PROCESS.md`, `docs/Lessons_Learned.md`, `docs/Glossary.md`
- **Why:** A branch name is not isolation. `checkout -b` in the shared project folder moves every chat using that folder onto the new branch and mixes uncommitted files.
- **What:** Default is `git worktree add ..\<RepoName>_<topic> -b wip/<topic>` and open the new chat **there**. Same-folder `checkout -b` is an explicit exception with a loud warning.
- **Benefit:** Improve code hygiene / documentation

### 2026-08-14 — New chat session owns a topic branch

- **Files:** `AGENTS.md`
- **Why:** Parallel chats on `main` mix hunks. Spawned specialists must not each grow a branch.
- **What:** Session start: purple multi-pick for `wip/<topic>` (Recommended + Stay on current branch + built-in Other) before the first edit. Subagents stay on the parent branch. Warn if other WIP would ride along; prefer a worktree when two chats share a folder.
- **Benefit:** Improve code hygiene / documentation

### 2026-08-13 — Change_Log screenshot thumbs (portable)

- **Files:** `docs/PROCESS.md`, `docs/Change_Log.md`, `AGENTS.md`, `scripts/promote_changelog_shot.py`, `scripts/capture_changelog_tabs.py`, `docs/changelog_shots/`, `tests/unit/test_promote_changelog_shot.py`
- **Why:** User-visible UI changes need a tracked progression, not only prose. Error dumps must stay out of git.
- **What:** PROCESS + Change_Log **Shot:** rule; promote script writes `docs/changelog_shots/*.jpg`; capture script is an app-bound stub. Sensitive views require `--allow-sensitive`.
- **Benefit:** Improve code hygiene / documentation

### 2026-08-10 — Rule of Three for literals; SQL one-liners; standards why

- **Files:** Coding_Standards.md, Lessons_Learned.md
- **Why:** Agents skip literal centralization and leave one-liner SQL in source; kit readers need to know standards are forced checklist items.
- **What:** Rule of Three table (fourth copy → nearest constant); SQL-in-files includes one-liners; loader safety + INFO load log called out. Lessons: Coding_Standards entries exist because Grok Build (and other LLMs) don’t apply them by default.
- **Benefit:** Improve code hygiene / documentation

### 2026-08-10 — SQL lives in files; cohesion pairs; process/DBA ownership

- **Files:** Coding_Standards.md, PROCESS.md, Database.md, AGENTS.md
- **Why:** Query text buried in app string literals blocks DBA review and duplicates migration discipline; portable kit should require the same fence as mature apps.
- **What:** Hard rule — multi-line SQL in `.sql` (or migration) files; DBA/schema lane owns statement text; app loads/runs. Cohesion pairs (SQL + loader). PROCESS migrations + Database wire steps aligned. Naming note: prefer inventory/report names over overloaded “health.”
- **Benefit:** Improve maintainability / Reduce technical debt / Improve code hygiene / documentation

### 2026-08-09 — Taste: Dijkstra / Northrop quotes

- **Files:** docs/Taste.md
- **Why:** Anchor kit judgment in classic engineering tenets, not fashion.
- **What:** Prefixed Taste.md with Dijkstra coding quotes (lines spent, simplicity, testing limits, abstraction, humility) and Jack Northrop’s efficient-and-beautiful line.
- **Benefit:** Improve code hygiene / documentation

### 2026-08-09 — Domain-neutral kit; setup links; light solo practices

- **Files:** README.md, Project.md, Database.md, Libraries.md, PROCESS.md, Glossary.md, Taste.md, Coding_Standards.md, AGENTS.md, skills READMEs, Lessons_Learned.md, .vscode/extensions.json
- **Why:** Template is a generic robust-app framework; product-domain examples and missing install links hurt portability.
- **What:** Removed Stock_Data / trading / broker-flavored wording; added Environment setup (Grok Build, Postgres, Python, VS Code extensions); lightweight solo/small-team practices; recommended extensions file.
- **Benefit:** Improve code hygiene / documentation; UX clarity for onboarding

### 2026-08-08 — Libraries + Database stubs; hard 500-line rule

- **Files:** Libraries.md, Database.md, Glossary.md, Coding_Standards.md, Project.md, README.md
- **Why:** Kit needed library menu, Postgres guidance, and absolute module-size rule.
- **What:** Libraries + Database decision tree (Postgres vs SQLite vs Timescale); Glossary library table; **500-line hard cap** (300 soft target); demo share caution for sensitive screenshots.
- **Benefit:** Improve code hygiene / documentation

### YYYY-MM-DD — Staff kit bootstrap

- **Files:** AGENTS.md, docs/*, Project.md, tests/README.md
- **Why:** Establish portable process for agents and humans.
- **What:** Copied LLM_Project_Template staff kit; filled intake placeholders as needed.
- **Benefit:** Improve code hygiene / documentation
