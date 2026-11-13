# Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| Duplicate CDC events | Financial overstatement | Idempotent consumers + unique keys |
| Kafka lag | Stale monitoring | Lag alerts + autoscaling |
| Schema drift | Pipeline failures | Contracts + compatibility checks |
| PII exposure | Compliance/security | RBAC + masking + secrets |
| Failed reconciliation | Incorrect reporting | Block publication + alert Finance |
| Experiment contamination | Invalid decision | Stable assignment + one-variant rule |
