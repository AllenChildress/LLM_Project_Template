# Recommended libraries (Python staff kit)

Pick by product needs (see [Project.md](../Project.md) intake). This is a **starter menu**, not a mandate.

## Core (most Python apps)

| Library | Why |
|---------|-----|
| **Python 3.11+** (3.12 preferred) | Modern typing, performance |
| **pytest** | Unit / integration / smoke |
| **python-dotenv** | Local `.env` without committing secrets |
| **requests** or **httpx** | HTTP APIs (httpx if async later) |
| **pydantic** (optional) | Validated config / API models |

## Desktop UI (if intake = desktop)

| Library | Why |
|---------|-----|
| **PyQt6** or **PySide6** | Mature desktop UI |
| **Qt WebEngine** (optional) | Embedded HTML / charts |

## Web UI (if intake = web)

| Library | Why |
|---------|-----|
| **FastAPI** or **Flask** | API / light web |
| **SQLAlchemy** or raw SQL | DB access layer |

## Data / analytics (if needed)

| Library | Why |
|---------|-----|
| **pandas** | Tables, time series, joins |
| **numpy** | Numeric arrays |
| **pandas-ta** or **ta-lib** | Technical indicators (trading-ish apps) |

## Database drivers

| Choice | Driver / notes |
|--------|----------------|
| **PostgreSQL** | `psycopg` (v3) — general default for multi-user apps |
| **SQLite** | stdlib `sqlite3` — single-user, local, simple |
| **TimescaleDB** | Postgres extension — **time-series / bars / IoT** (see [Database.md](Database.md)) |

## Do not commit

Lockfiles (`requirements.txt` / `pyproject.toml`) yes; `.env` and secrets no.

Wire libraries in the app’s own dependency file after intake — this kit only documents the menu.
