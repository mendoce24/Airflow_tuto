from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime

with DAG(
        dag_id='7.2-externalTaskSensor',
        description='Secondary Dag',
        schedule_interval="@daily",
        start_date= datetime(2023, 9, 1),
        end_date= datetime(2023, 9, 19),
        max_active_runs= 1) as dag:

    t1 = ExternalTaskSensor(task_id='wating_dag',
                external_dag_id= "7.1-externalTaskSensor",
                external_task_id= "task1",
                poke_interval=10)
    
    t2 = BashOperator(task_id='task2',
                  bash_command= "sleep 10 && echo 'DAG 2 finished!'",
                  depends_on_past= True)
    

t1 >> t2