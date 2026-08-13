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
