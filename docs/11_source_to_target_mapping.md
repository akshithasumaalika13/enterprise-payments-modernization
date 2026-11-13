# Source-to-Target Mapping

| Source | Source Field | Target | Target Field | Rule |
|---|---|---|---|---|
| PostgreSQL payments | payment_id | fct_payments | payment_id | Direct |
| PostgreSQL payments | amount | fct_payments | amount | Decimal(14,2), >0 |
| PostgreSQL payments | status | fct_payments | status | Uppercase accepted values |
| Product events | event_name | fct_funnel | funnel stage | Map event to stage |
| Product events | variant | fct_experiment_results | variant | CONTROL/TREATMENT |
