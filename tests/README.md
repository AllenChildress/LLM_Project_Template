# Tests

```text
tests/
  unit/           # fast, isolated
  integration/    # cross-module / local services
  smoke/          # boot + critical path
```

## Conventions

- Prefer unit tests for new logic.
- Integration when contracts cross packages or need a real local DB.
- Smoke when “does the app still start / critical UI path work?” matters.
- Keep secrets out of fixtures; use env or local-only config.

## Running (example)

```powershell
# Adjust to your runner
python -m pytest tests/unit -q
```

Add a thin suite script under `scripts/testing/` when the app grows.
