from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='bashoperator',
    description='using bash operator',
    start_date= datetime(2023, 9, 18)) as dag:
    t1 = BashOperator(task_id='hello_with_bash',
                  bash_command= "echo 'hello people!'")
t1