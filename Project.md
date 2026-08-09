# Project — staff kit spine

**Purpose:** One file to drop into (or copy from) a new VS Code project so Grok Build and humans share the same expectations.

**How to use with an agent**

1. Paste or open this file.
2. Answer **§ Intake** (or use multi-choice prompts if the agent offers them).
3. Ask: *“Implement the staff kit for this repo based on my intake answers and the stubs under docs/.”*
4. Agent fills templates, skips declined sections, writes a short Change_Log row for the bootstrap.

---

## Intake (ask the developer)

Copy answers under each line or reply in chat.

### Product

- [ ] App name / one-sentence purpose: _______________
- [ ] Primary language(s): _______________
- [ ] UI? (none / CLI / desktop / web): _______________
- [ ] Database? (none / SQLite / Postgres / other): _______________
- [ ] External APIs / auth?: _______________

### Kit modules (include?)

| Module | Include? | Notes |
|--------|----------|--------|
| AGENTS.md + spawn routing | Y / N | Multi-agent |
| PROCESS.md | Y / N | Always recommended |
| Coding_Standards.md | Y / N | Always recommended |
| Change_Log.md | Y / N | User-visible history |
| Glossary.md | Y / N | Shared words |
| ToDo.md (+ Done) | Y / N | Backlog |
| Lessons_Learned.md | Y / N | Scar tissue |
| Taste.md | Y / N | Judgment |
| Logging norms | Y / N | Levels / story vs construction |
| tests unit/integration/smoke | Y / N | |
| pytest + suite script later | Y / N | |
| Screenshot smoke (UI apps) | Y / N | |
| DB schema + migrations pattern | Y / N | See [docs/Database.md](docs/Database.md) |
| Backup script pattern | Y / N | |
| Recommended libraries list | Y / N | [docs/Libraries.md](docs/Libraries.md) |
| Domain skills folder | Y / N | Trading, etc. |
| Multi-agent specialists | Y / N | ui/dba/tester/… |

### Constraints

- Prefer short agent replies? Y / N  
- Commit message trailers (`Assisted-by: …`)? Y / N  
- Default: **do not push** until human asks? Y / N  

---

## Target file set (after intake)

```text
AGENTS.md
docs/PROCESS.md
docs/Coding_Standards.md
docs/Change_Log.md
docs/Glossary.md
docs/ToDo.md
docs/Lessons_Learned.md
docs/Taste.md                    # optional
docs/skills/General/…            # optional playbooks
docs/skills/Domain/…             # optional
tests/{unit,integration,smoke}/
```

App-specific docs (schema, runbooks, product ADRs) stay **outside** this kit once the app grows.

---

## Skeleton rules (agent implements)

1. **Never load the whole docs set** into context — open only files named by AGENTS / task.
2. **One Change_Log entry per user-visible change** (Why / What / Benefit).
3. **ToDo** updated when backlog items complete or cancel.
4. **Module size:** prefer files under ~500 lines; split by purpose (not arbitrary chops).
5. **Tests:** new behavior → unit first; cross-layer → integration; UI shell → smoke.
6. **Secrets:** never commit `.env`, tokens, dumps.
7. **Generic vs specific:** kit files stay portable; product truth lives in the app repo.

---

## Public sharing / meetup (careful)

| Usually OK | Avoid |
|------------|--------|
| Staff kit (this repo) | Secrets, tokens, `.env` |
| Generic chart / options UI demos | **Account History / statement / balances** screenshots |
| Architecture diagrams | Account numbers, last-4, tax lots in cleartext |
| Redacted process docs | Full personal Change_Log dumps |

Charts and options screens can still leak **trade overlays** — crop or use a throwaway watchlist when presenting.

---

## Meetup talk track (optional agenda)

Use this kit as the demo spine (not Stock_Data internals).

1. Grok Build in VS Code + GitHub  
2. Skill / staff files: AGENTS, PROCESS, Coding_Standards  
3. Documentation: Change_Log, Glossary  
4. Logging  
5. Testing (unit / smoke / integration, pytest, screenshots)  
6. Database (schema, migrations, backups) — if included  
7. Data model (session-style ownership over map sprawl) — if applicable  
8. UI patterns (tabs, status, refresh, log) — if applicable  
9. Performance (caching, honest limits of chart stacks)  
10. Self-assessment prompts (prompts on *prompts* and on *Change_Log*)  
11. Parallel work (agents + Python threads — different tools)  
12. Cost / ROI (fill your own numbers)

---

## Self-assessment prompts (exercises)

**#1 — Prompts:**  
*Looking at my prompts, what can you tell me about the type of programmer I am, my style, experience level, and areas for improvement?*

**#2 — Change_Log:**  
*Looking at Change_Log.md, what can you tell me about the type of programmer I am, my style, experience level, and areas for improvement?*

---

## OOP analogy: kit vs app docs

| Layer | Role | Example |
|-------|------|---------|
| **Base (this kit)** | Portable process | “Always keep a Change_Log” |
| **Subclass (app)** | Product instance | Stock_Data’s 500+ Change_Log rows, Schwab runbook |
| **Do not** | Merge product secrets into the kit | Tokens, account last-4, broker quirks |

When the app learns a **general** lesson, promote a short rule into this kit. When the lesson is **domain-only**, keep it in the app (or `docs/skills/Domain/`).

---

## Agent bootstrap prompt (copy-paste)

```text
Open Project.md and the stubs under docs/.
I answered intake as follows:
  <paste answers>

Implement the staff kit for this repository:
- Keep files portable (no personal secrets, no trading-specific content).
- Skip modules I set to N.
- Fill placeholders; leave TODO comments where I must supply product names.
- Add one Change_Log entry for this bootstrap.
Do not push unless I ask.
```
