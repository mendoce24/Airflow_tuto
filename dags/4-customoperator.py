from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator


with DAG(dag_id="customoperator", 
         description="Our first custom operator dag", 
         start_date= datetime(2023,9,18)) as dag:
    
    t1= HelloOperator(task_id="Hello", 
                      name="Cesar")

t1