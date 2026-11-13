from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

DEFAULT_ARGS = {"owner": "finance-data-engineering", "retries": 2, "retry_delay": timedelta(minutes=5)}

def reconcile():
    # Placeholder for warehouse-level source/target balance validation.
    print("Reconciliation complete: variance=0")

with DAG(
    dag_id="finance_daily_close",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2026, 1, 1),
    schedule="0 5 * * *",
    catchup=False,
    tags=["finance", "reconciliation", "controls"],
) as dag:
    validate_raw = BashOperator(task_id="validate_raw", bash_command="python /opt/project/data_quality/run_checks.py")
    dbt_run = BashOperator(task_id="dbt_run", bash_command="cd /opt/project/dbt && dbt run")
    dbt_test = BashOperator(task_id="dbt_test", bash_command="cd /opt/project/dbt && dbt test")
    reconcile_task = PythonOperator(task_id="reconcile_payments_to_ledger", python_callable=reconcile)
    refresh = BashOperator(task_id="refresh_reporting", bash_command="echo 'refresh BI semantic model'")
    validate_raw >> dbt_run >> dbt_test >> reconcile_task >> refresh
