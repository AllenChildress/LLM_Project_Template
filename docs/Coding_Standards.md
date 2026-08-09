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
- Rule of Three: wait for three real uses before extracting shared helpers (unless duplication is already dangerous).

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

## Security

- Secrets only in env / secret store; never in git.
- Redact tokens in logs and error reports.
