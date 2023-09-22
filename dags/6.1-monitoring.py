from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime


def myfunction():
    pass


with DAG(dag_id='6.1-monitoring',
        description='monitoring our DAG',
        schedule_interval= "@daily",
        start_date= datetime(2023, 9, 1), 
        end_date= datetime(2023, 9, 18)) as dag:

    t1 = BashOperator(task_id='task1',
                  bash_command= "sleep 2 && echo 'Task 1'")

    t2 = BashOperator(task_id='task2',
                  bash_command= "sleep 2 && echo 'Task 2'")

    t3 = BashOperator(task_id='task3',
                  bash_command= "sleep 2 && echo 'Task 3'")

    t4 = PythonOperator(task_id='task4',
                  python_callable= myfunction)

    t5 = BashOperator(task_id='task5',
                  bash_command= "sleep 2 && echo 'Task 5'")
    
t1 >> t2 >> t3>> t4>> t5