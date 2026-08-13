# Coding standards (portable skeleton)

Fill language-specific sections when you adopt this kit. Keep this file **general** enough to copy.

## Language / style

- Prefer explicit imports; avoid `import *`.
- Type hints on public APIs (Python 3.11+ recommended).
- Meaningful names; refuse clever abbreviations in public APIs.

## Errors

- Prefer one place to map external failures → user-safe messages.
- Log detail for operators; never log secrets (tokens, passwords, full auth headers).

## Module size (hard rule — all projects, all languages)

- **Hard cap: 500 lines** per source module (soft target **300** when practical).
- Applies to **every** language and stack this kit is copied into — no exceptions for “just one more helper.”
- Split by **purpose** (e.g. surface vs build vs incremental), not arbitrary line chops.
- A clear name beats a mega-mixin that “does everything UI.”
- Generated code / vendored third-party: exclude from the cap; **your** code is not exempt.

## OOP / state

- Prefer **named objects** that own live state over parallel `dict[str, …]` caches for the same entity.

## Rule of Three (helpers **and** literals)

| Count | What to do |
|-------|------------|
| **Once** | Fine inline. |
| **Twice** | OK for tiny snippets or one-off literals. |
| **Three** | Strong signal to centralize (helper or named constant). |
| **Four or more** | **Must** be a named constant or helper, scoped **as closely as possible** (function → module → package). |

If extracting **adds net lines** without clarity, you over-engineered it.

**Literals / enterprise:** small projects stop at module constants. Multi-language enterprise apps later externalize the same strings into resource/config files — do not build i18n early, but do not keep the fourth copy of the same literal either.

## UI (if applicable)

- Named debounce constants for gesture-driven reloads.
- Status text should answer: what is happening, and is it done?

## Logging

- **INFO** (or your “story” level): user-recognizable outcomes.
- **DEBUG**: construction / poll noise.
- Optional **CODE** (or similar): start/end landmarks for work a human can map to the UI (view, refresh, save) with `elapsed_ms`.
- Do not demote real failures to WARN when the surface is broken.

## Tests

- Mirror package layout under `tests/unit/…` when practical.
- Fixtures over copy-paste setup.
- UI smokes: scripted screenshot optional; assert process stays up and critical widgets exist.
- User-visible view/tab paint: promote a Change_Log **Shot:** (PROCESS § Screenshots). Do not commit `error_*` dumps.

## Security

- Secrets only in env / secret store; never in git.
- Redact tokens in logs and error reports.

## Cohesion pairs (delete-together)

When placing or moving code, ask: **if this is deleted, what else must go with it?** Keep those pieces in one package (or one obvious pair) so the next agent does not leave orphans.

| Pair | Live together | Why |
|------|---------------|-----|
| SQL text + loader | `db/` or `src/.../sql/*.sql` + the small loader that reads them | Loader exists only to load statements; keep it next to the files |
| Domain type + table DDL | Domain model + matching schema SQL when introduced | Parity stays discoverable |

Adapt paths to your layout; the rule is **colocate dependents**, not a fixed directory name.

## SQL lives in files (hard rule — DBA / schema lane owns the text)

**Do not** leave SQL as string literals in application code — **including one-liners**. SQL changes over time; keep it in `.sql` files. Load by name from a small loader next to those files.

| Own | Where |
|-----|--------|
| **DBA / database lane** | Statement text, schema, indexes, upserts, report queries as `.sql` files |
| **App / UI / store code** | Call the named statement, map rows, handle errors — not invent SQL strings in-line |

**Schema migrations** use the same idea: versioned SQL (or your migration tool’s files), not DDL pasted into app source. See [PROCESS.md](PROCESS.md) § Migrations / schema and [Database.md](Database.md).

**Allowed exceptions (narrow):** only SQL that **cannot** be a static file (safe identifier quoting via the driver, or a template file with a placeholder for an allow-listed dynamic fragment). Never concatenate user/config text into SQL.

**Loader duties (when you implement one):** path stay-inside SQL dir; reject empty/null/BOM footguns from hand edits; log a compact **INFO** line on first load (filename + size + short preview).

**Why:** Reviewers and the database owner can change queries without spelunking app code.

**Names:** Prefer names that say what the code does (`data_inventory`, `db_report`). Avoid overloaded words (e.g. medical “health”) unless that is the product domain.
