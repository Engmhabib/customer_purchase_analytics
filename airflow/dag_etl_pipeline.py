from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': True,
    'email': ['data-team@company.com']
}

dag = DAG(
    'customer_purchase_etl',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

ingest_data = DatabricksRunNowOperator(
    task_id='ingest_data',
    databricks_conn_id='databricks_default',
    job_id='123',  # Job ID from Databricks workspace
    notebook_params={"step": "ingest"},
    dag=dag
)

transform_data = DatabricksRunNowOperator(
    task_id='transform_data',
    databricks_conn_id='databricks_default',
    job_id='124',
    notebook_params={"step": "transform"},
    dag=dag
)

load_to_sql = DatabricksRunNowOperator(
    task_id='load_to_sql',
    databricks_conn_id='databricks_default',
    job_id='125',
    notebook_params={"step": "load"},
    dag=dag
)

ingest_data >> transform_data >> load_to_sql
