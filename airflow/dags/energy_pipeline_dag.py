from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from app.ingestion.fetch_energy_prices import run_ingestion


def dummy_validation():
    print("Validation stage placeholder")


with DAG(
    dag_id="global_energy_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={
        "retries": 3,
        "retry_delay": timedelta(minutes=5)
    },
    tags=["energy", "etl", "mongodb"]
):

    ingest_task = PythonOperator(
        task_id="ingest_energy_prices",
        python_callable=run_ingestion
    )

    validate_task = PythonOperator(
        task_id="validate_data",
        python_callable=dummy_validation
    )

    ingest_task >> validate_task