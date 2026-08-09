# Database (portable stubs)

## Is PostgreSQL right for “most” Python projects?

| Use case | Good default | Why |
|----------|--------------|-----|
| Multi-user app, migrations, integrity, concurrent writers | **PostgreSQL** | Mature, free, excellent tooling, strong SQL |
| Local single-user tool, simple storage | **SQLite** | Zero server, one file |
| Heavy **time-series** (bars, metrics every minute, retention) | **Postgres + TimescaleDB** (or similar) | Hypertables, compression, time-oriented queries |
| Huge analytics warehouse | Often **not** OLTP Postgres alone | Consider warehouse tools later |

**Stock_Data chose Postgres/Timescale** because equities bars + analytics are time-series at volume, with multi-scale materialize and retention. That is **not** a claim that every Python app needs Timescale.

**Generic rule:** start with **Postgres** if you need a real server DB; start with **SQLite** if you need “no install.” Add Timescale only when time-series workload justifies it.

---

## Intake (agent asks)

- [ ] DB? none / SQLite / PostgreSQL / Postgres+Timescale / other  
- [ ] Local only or remote host?  
- [ ] Need backups? Y / N  
- [ ] Need migrations/versioned schema? Y / N  

---

## PostgreSQL — install & wire (Windows sketch)

1. Install Postgres (installer or package manager). Note port (default **5432**), superuser password.
2. Create a role + database for the app (not superuser for daily use).
3. App `.env` (never commit):

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=your_app
POSTGRES_USER=your_app
POSTGRES_PASSWORD=...
# or DATABASE_URL=postgresql://user:pass@localhost:5432/your_app
```

4. Python: `pip install psycopg[binary]` (or poetry/uv equivalent).
5. Schema: keep SQL under `db/` or `src/.../sql/` with a version note; apply via script or migration tool.
6. Backup: `pg_dump` on a schedule before destructive migrations.

### Optional TimescaleDB

- Install Timescale extension into the same Postgres instance.
- Use for hypertables on time + symbol style data — only if intake says time-series heavy.

---

## SQLite stub

- File path in config (e.g. `data/app.db`).
- stdlib `sqlite3` or SQLAlchemy.
- Fine for single writer; careful with concurrent UI + workers.

---

## Other DBs

| Engine | When to consider |
|--------|------------------|
| MySQL / MariaDB | Existing shop standard |
| SQL Server | Windows enterprise shops |
| MongoDB | Document-shaped data (not a free “no schema” pass) |

Add a short `docs/Database_<Engine>.md` only when chosen — keep this file as the decision tree.

---

## Schema / UI inventory (optional later)

- Versioned DDL + Change_Log when schema changes.
- Optional admin UI tab listing tables/row counts (app-specific).
