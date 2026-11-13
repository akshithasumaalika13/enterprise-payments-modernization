# Production Runbook

## Reconciliation failure
1. Stop publication of Finance dashboard refresh.
2. Compare source payment total to ledger and warehouse totals.
3. Review duplicate/missing IDs and late-arriving settlements.
4. Re-run failed Airflow task after root cause is corrected.
5. Record incident and control evidence.

## Kafka lag
1. Inspect consumer lag and broker health.
2. Verify downstream Snowflake/S3 availability.
3. Scale consumers if backlog is genuine load.
4. Replay dead-letter events only after idempotency checks.

## Data freshness breach
1. Identify latest successful partition/load timestamp.
2. Check Airflow task logs and API source availability.
3. Notify business owner if SLA will be missed.
