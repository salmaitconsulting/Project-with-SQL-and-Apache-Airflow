from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello Airflow!")

with DAG(
    dag_id='test1',
    start_date=datetime(2026, 4, 2),
    schedule='@daily',
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='say_hello',
        python_callable=hello
    )



