from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def print_hello():
    print("Hello people of BeCode")

with DAG(dag_id="pythonoperator", 
         description="Our first dag using Pyhon Operator", 
         schedule_interval="@once",
         start_date= datetime(2023,9,18)) as dag:
    
    t1 = PythonOperator(task_id="hello_with_paython",
                        python_callable=print_hello)
t1