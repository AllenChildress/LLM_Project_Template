# Project_Template — staff kit (portable)

A **generic** VS Code / Grok Build starter kit: process, agents, docs hygiene, testing layout, and logging norms you can copy into any Python project.

**Not** application code. **Not** trading or Stock_Data product docs.

| Audience | Use |
|----------|-----|
| **You** | Clone/copy into a new repo; answer intake in [Project.md](Project.md); fill stubs. |
| **Meetup** | Share this kit as “how I run agent-assisted projects.” |
| **Grok Build** | Open *this* folder as the workspace to edit the kit without polluting app repos. |

## Quick start

1. Copy this folder (or clone) as the start of a new project **or** merge selected files into an existing repo.
2. Open the folder in VS Code + Grok Build.
3. Read **[Project.md](Project.md)** — answer the intake questions (or paste them to the agent).
4. Agent implements from the stubs under `docs/` and root `AGENTS.md`.
5. Replace placeholders (`YOUR_APP`, `YOUR_NAME`) and delete sections you declined in intake.

## Layout

```text
Project_Template/
  README.md                 # this file
  Project.md                # intake + skeleton + talk track
  AGENTS.md                 # short agent entry (main thread)
  docs/
    PROCESS.md              # how work is done
    Coding_Standards.md     # style, errors, module size
    Change_Log.md           # user-visible history template
    Glossary.md             # shared vocabulary (start empty-ish)
    ToDo.md                 # backlog / Done
    Lessons_Learned.md      # durable scars (general section first)
    Taste.md                # judgment / “who is the computer”
    skills/
      README.md             # what belongs in skills vs docs
      General/              # portable playbooks
      Domain/               # empty — project-specific skills later
  tests/
    README.md               # unit / integration / smoke
    unit/
    integration/
    smoke/
  .gitignore
```

## Staff kit vs skills vs app docs

| Kind | What it is | Lives |
|------|------------|--------|
| **Staff kit** | How *any* project is run with humans + agents | This template (copy into each app) |
| **Skills** | Playbooks you paste/attach for a *task* (often domain) | `docs/skills/…` |
| **App docs** | This product’s Change_Log, schema, runbooks | App repo only (e.g. Stock_Data) |

## Relationship to Stock_Data

Stock_Data is a **worked example**, not the kit. Keep product docs there. Improve the kit here, then copy improvements into apps when ready.

## License / sharing

Treat as your personal portable process unless you add a LICENSE. Redact any secrets before publishing.
