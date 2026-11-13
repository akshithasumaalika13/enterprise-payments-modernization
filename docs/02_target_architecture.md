# Target Architecture

```mermaid
flowchart LR
  PG[(PostgreSQL)] --> D[Debezium]
  D --> K[Kafka]
  API[External APIs] --> K
  K --> S3[(AWS S3 Bronze)]
  S3 --> SP[Spark/PySpark]
  SP --> WH[(Snowflake)]
  WH --> DBT[dbt]
  DBT --> F[Finance Marts]
  DBT --> P[Product Marts]
  DBT --> R[Risk Marts]
  F --> BI[Power BI/Tableau]
  P --> BI
  R --> BI
  AF[Airflow] --> WH
  AF --> DBT
  OM[OpenMetadata] -. lineage .-> DBT
  PR[Prometheus/Grafana] -. monitor .-> API
```

## Design principles
- Batch + streaming
- Reproducible infrastructure
- Automated testing and controls
- Least-privilege access
- Business-owned metrics
- End-to-end lineage
