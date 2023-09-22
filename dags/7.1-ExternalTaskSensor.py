from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
        dag_id='7.1-externalTaskSensor',
        description='Main Dag',
        schedule_interval="@daily",
        start_date= datetime(2023, 9, 1),
        end_date= datetime(2023, 9, 19)) as dag:

    t1 = BashOperator(task_id='task1',
                  bash_command= "sleep 10 && echo 'DAG finalizado!'",
                  depends_on_past= True)
t1