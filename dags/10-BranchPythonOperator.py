from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, date

default_args = {
'start_date': datetime(2023, 8, 20),
'end_date': datetime(2023, 8, 25)
}

def _choose(**context):
    if context["logical_date"].date() < date(2023, 8, 23):
        return "finish_22_aug"
    return "start_23_aug"

with DAG(dag_id="10-branching",
    schedule_interval="@daily",
	default_args=default_args
) as dag:

    branching = BranchPythonOperator(task_id="branch",
	                                 python_callable=_choose)

    finish_22 = BashOperator(task_id="finish_22_aug",
	                         bash_command="echo 'Running {{ds}}'")

    start_23 = BashOperator(task_id="start_23_aug",
	                        bash_command="echo 'Running {{ds}}'")

    branching >> [finish_22, start_23]