from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id= "firstdag",
    description="Our first DAG", 
    start_date=datetime(2023, 9, 14), 
    schedule_interval="@once") as dag:
    t1 = EmptyOperator(task_id="dummy")
t1
