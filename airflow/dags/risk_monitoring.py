from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def risk_monitoring_task():
    print("Risk monitoring pipeline executed successfully")


with DAG(
    dag_id="risk_monitoring_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    monitor_risk = PythonOperator(
        task_id="monitor_risk",
        python_callable=risk_monitoring_task,
    )
