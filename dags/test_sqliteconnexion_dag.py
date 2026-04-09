from datetime import datetime
from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator


default_args = {
    'owner': 'salima',
    'start_date': datetime(2026, 4, 3),
    'catchup': False
}

with DAG(
    dag_id='test_sqlite_connection',
    default_args=default_args,
    schedule_interval=None,  # Exécution manuelle
) as dag:

    test_task = SqliteOperator(
        task_id='test_sqlite',
        sqlite_conn_id='my_sqlite_conn',  # votre connection
        sql="SELECT 1;"
    )
