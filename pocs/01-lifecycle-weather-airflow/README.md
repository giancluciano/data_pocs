# Data Engineering Lifecycle — weather pipeline with Airflow

- **Roadmap phase:** 01 — Introduction (Data Engineering Lifecycle) · also first contact with 08 — Apache Airflow
- **Doc note:** [`docs/01-data-engineering-lifecycle.md`](../../docs/01-data-engineering-lifecycle.md)
- **Status:** in progress

## Goal

Walk through every stage of the data engineering lifecycle once, at the most basic level,
with Airflow orchestrating it:

| Lifecycle stage | In this POC |
|---|---|
| Generation | [Open-Meteo](https://open-meteo.com/) public weather API (no key) |
| Ingestion | Airflow task calls the API and lands the response as-is |
| Storage | SQLite file (`data/weather.db`, git-ignored) |
| Transformation | `raw` → `clean` (typed, one row per city+hour) → `daily` aggregate |
| Serving | A SQL query / CSV export answering a simple question (e.g. daily min/max temp per city) |

Airflow focus for this POC: **DAGs, tasks, dependencies** (TaskFlow `@task`, `>>`, XComs).
Scheduling/backfills, idempotency and Variables/Connections are left for later POCs.

## Stack

- Apache Airflow (official Docker Compose setup)
- Python (inside the Airflow image — no local Airflow install needed)
- SQLite (target database for the weather data — **not** Airflow's metadata DB, which is Postgres in the compose stack)
- Open-Meteo Forecast API: `https://api.open-meteo.com/v1/forecast`

## Plan (my checklist)

- [ ] Explore the API by hand (browser/`curl`): pick 1–3 cities, choose hourly variables, read the JSON shape
- [ ] Bring up Airflow with Docker Compose and open the UI
- [ ] First DAG: a single "hello" task, see it run in the UI and read its logs
- [ ] `extract` task: call the API, return/land the raw payload
- [ ] `load_raw` task: store raw rows in SQLite
- [ ] `transform_clean` task: typed hourly table
- [ ] `transform_daily` task: daily aggregate table
- [ ] Wire dependencies: `extract >> load_raw >> transform_clean >> transform_daily`
- [ ] Serving: query the `daily` table and write down the answer
- [ ] Write the doc note

## Questions to answer while building

- Where does each lifecycle stage start and end in my DAG?
- What does Airflow actually do vs. what my Python code does?
- What passes between tasks (XCom) and what should go through storage instead? Why?
- What happens if I trigger the DAG twice — do I get duplicate rows?

## How to run

```bash
```

## Results / takeaways
