from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

templated_command = """
{% for file in filenames %}
"""

with DAG(
        dag_id='8.templating',
        description='Example using templates',
        schedule_interval="@daily",
        start_date= datetime(2023, 9, 18),
        end_date= datetime(2023, 9, 19),
        max_active_runs= 1) as dag:

    t1 = BashOperator(task_id='task1',
                  bash_command= templated_command,
                  depends_on_past= True)


t1