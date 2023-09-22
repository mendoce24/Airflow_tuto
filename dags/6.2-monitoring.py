from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime


def myfunction():
    raise Exception

default_args = {}

with DAG(dag_id='6.2-monitoring',
        description='monitoring our DAG',
        schedule_interval= "@daily",
        start_date= datetime(2023, 9, 1), 
        end_date= datetime(2023, 9, 18), 
        default_args= default_args,
        max_active_runs=1) as dag:

    t1 = BashOperator(task_id='task1',
                  bash_command= "sleep 2 && echo 'Task 1'",
                  trigger_rule= TriggerRule.ALL_SUCCESS,
                  retries= 2,
                  retry_delay= 5,
                  depends_on_past= False)

    t2 = BashOperator(task_id='task2',
                  bash_command= "sleep 2 && echo 'Task 2'", 
                  retries= 2,
                  retry_delay= 5,
                  trigger_rule= TriggerRule.ALL_SUCCESS, 
                  depends_on_past= True)

    t3 = BashOperator(task_id='task3',
                  bash_command= "sleep 2 && echo 'Task 3'", 
                  retries= 2,
                  retry_delay= 5,
                  trigger_rule= TriggerRule.ALWAYS, 
                  depends_on_past= True)

    t4 = PythonOperator(task_id='task4',
                  python_callable= myfunction, 
                  retries= 2,
                  retry_delay= 5,
                  trigger_rule= TriggerRule.ALL_SUCCESS, 
                  depends_on_past= True)

    t5 = BashOperator(task_id='task5',
                  bash_command= "sleep 2 && echo 'Task 5'", 
                  retries= 2,
                  retry_delay= 5,
                  depends_on_past= True)
    
t1>> t2 >> t3>> t4>> t5