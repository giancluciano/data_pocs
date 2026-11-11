# data_pocs

Personal data engineering study repo, following the
[roadmap.sh Data Engineer roadmap](https://roadmap.sh/data-engineer).

- **`pocs/`** — hands-on proofs of concept, one folder per topic/experiment.
- **`docs/`** — my own summaries of what I learned, one note per topic.

> **Rule of this repo:** all code and notes here are written by me.
> AI is only used to organize topics, set up the environment, and maintain this README.

## Structure

```
data_pocs/
├── README.md              # this file: roadmap checklist + progress
├── docs/
│   ├── _template.md       # template for a study note
│   └── NN-topic-name.md   # one note per topic (NN = roadmap phase)
└── pocs/
    ├── _template/         # template for a new POC
    └── NN-topic-name/     # one folder per POC, self-contained
```

### Conventions

- Prefix docs and POCs with the **phase number** below (e.g. `03-postgresql`, `08-airflow-first-dag`).
- Each POC is **self-contained**: its own `README.md`, dependencies (`pyproject.toml` / `requirements.txt`) and `docker-compose.yml` when it needs services.
- Each POC links to its doc note, and vice versa.
- Tick the checklist below when a topic has a doc note (and a POC, when it makes sense).
- Secrets go in a local `.env` (git-ignored), never committed.

## Environment

| Tool | Version | Notes |
|------|---------|-------|
| Python | 3.14.2 (pyenv) | one virtualenv per POC (`.venv/`, git-ignored) |
| Docker / Compose | Compose v5.6.0 | for databases, Kafka, Airflow, Spark, etc. |
| Git | — | commits follow `type: description` (feat, docs, chore…) |

Typical POC setup:

```bash
cd pocs/NN-topic-name
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt     # if any
docker compose up -d                # if the POC needs services
```

## Roadmap progress

Legend: `[ ]` not started · `[~]` in progress · `[x]` done (doc written)

### 01 — Introduction
- [ ] What is Data Engineering
- [ ] Data Engineering vs Data Science
- [ ] Skills & Responsibilities
- [~] Data Engineering Lifecycle (generation → storage → ingestion → transformation → serving)
- [ ] Choosing the right technologies

### 02 — Foundations
- [ ] Programming skills — Python (main), Java / Scala / Go (awareness)
- [ ] Data structures & algorithms
- [ ] SQL
- [ ] Git & GitHub
- [ ] Linux basics
- [ ] Networking fundamentals
- [ ] Distributed systems basics

### 03 — Databases
- [ ] Database fundamentals
- [ ] Relational databases — PostgreSQL, MySQL, MariaDB, MS SQL, Oracle
- [ ] Transactions
- [ ] Indexing
- [ ] Data normalization
- [ ] Data modelling techniques
- [ ] CAP theorem
- [ ] Horizontal vs vertical scaling
- [ ] NoSQL — Document (MongoDB, CouchDB)
- [ ] NoSQL — Column (Cassandra, HBase, Bigtable)
- [ ] NoSQL — Key-value (Redis, DynamoDB, Memcached)
- [ ] NoSQL — Graph (Neo4j, Neptune)
- [ ] Elasticsearch

### 04 — Data Warehousing & Data Lakes
- [ ] What is a data warehouse
- [ ] OLTP vs OLAP
- [ ] Star vs snowflake schema
- [ ] Slowly Changing Dimensions (SCD)
- [ ] Data mart
- [ ] Data warehouse architectures
- [ ] Warehouses — Snowflake, BigQuery, Redshift
- [ ] Data lake
- [ ] Lakehouse — Databricks Delta Lake, Onehouse
- [ ] Data mesh, data fabric, data hub
- [ ] Metadata-first architecture

### 05 — Data Ingestion & Pipelines
- [ ] Sources of data — databases, APIs, logs, mobile apps, IoT
- [ ] Data collection considerations
- [ ] Types of ingestion — batch, streaming, realtime, hybrid
- [ ] Data pipelines
- [ ] ETL — extract, transform, load
- [ ] ETL vs Reverse ETL — Hightouch, Census, Segment
- [ ] Idempotency
- [ ] Declarative vs imperative

### 06 — Messaging & Streaming
- [ ] Messaging systems
- [ ] Async vs sync communication
- [ ] Messages vs streams
- [ ] Apache Kafka
- [ ] RabbitMQ
- [ ] AWS SQS / SNS

### 07 — Big Data & Cluster Computing
- [ ] Cluster computing basics
- [ ] Distributed file systems — HDFS
- [ ] MapReduce
- [ ] YARN
- [ ] Apache Spark
- [ ] Managed processing — Dataflow, Glue ETL, Data Factory

### 08 — Orchestration & Transformation
- [ ] Job scheduling
- [ ] Apache Airflow
- [ ] Prefect
- [ ] Luigi
- [ ] dbt

### 09 — Cloud & Infrastructure
- [ ] Cloud computing & cloud architectures
- [ ] Serverless options
- [ ] AWS — EC2, S3, RDS, Aurora, EKS
- [ ] GCP — Compute Engine, Cloud Storage, Cloud SQL, GKE, Deployment Manager
- [ ] Azure — Virtual Machines, Blob Storage, SQL Database, CosmosDB
- [ ] Containers — Docker
- [ ] Orchestration — Kubernetes
- [ ] Infrastructure as Code — Terraform, OpenTofu, AWS CDK

### 10 — CI/CD & Testing
- [ ] CI/CD — GitHub Actions, GitLab CI, CircleCI, ArgoCD
- [ ] Unit testing
- [ ] Integration testing
- [ ] Functional & end-to-end testing
- [ ] Smoke & load testing
- [ ] A/B testing

### 11 — Data Quality, Governance & Security
- [ ] Data quality
- [ ] Data lineage
- [ ] Metadata management
- [ ] Data interoperability
- [ ] Authentication vs authorization
- [ ] Encryption, masking, obfuscation, tokenization
- [ ] Regulations — GDPR, ECPA, EU AI Act

### 12 — Monitoring & Observability
- [ ] Monitoring concepts
- [ ] Prometheus
- [ ] Datadog, New Relic, Sentry

### 13 — Data Serving
- [ ] Business intelligence — Tableau, Power BI, Looker, Streamlit
- [ ] Data analytics
- [ ] Machine learning & MLOps

---

Topic list sourced from the official roadmap content
([kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap), `roadmaps/data-engineer`) on 2026-11-09.
Phases are my own grouping for study order.

## POC index

| # | POC | Topic | Doc | Status |
|---|-----|-------|-----|--------|
| 01 | [lifecycle-weather-airflow](pocs/01-lifecycle-weather-airflow/) | Data Engineering Lifecycle + Airflow basics (Open-Meteo → SQLite) | [note](docs/01-data-engineering-lifecycle.md) | in progress |
