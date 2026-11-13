# Testing Strategy

- Unit tests: event-processing and validation logic
- Contract tests: required event fields and schemas
- dbt tests: uniqueness, not-null, accepted values, referential integrity
- Reconciliation tests: source totals vs ledger totals
- Integration tests: API -> Kafka -> warehouse path
- Smoke tests: API health and core metrics after deployment
- UAT: Finance validates reconciliation; Product validates funnel and experiment definitions
