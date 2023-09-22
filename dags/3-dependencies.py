from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def print_hello(msg):
    print(msg)

with DAG(dag_id="dependencies", 
         description="Our first dag using dependencies between task", 
         schedule_interval="@once",
         start_date= datetime(2023,9,18)) as dag:
    
    t1 = PythonOperator(task_id="task1",
                        python_callable=print_hello,
                        provide_context=True,
                        op_kwargs= {'msg' : "Hello people of BeCode"})
    
    t2 = PythonOperator(task_id="task2",
                        python_callable=print_hello,
                        provide_context=True,
                        op_kwargs= {'msg' : "Hello task 2"})
    
    t3 = PythonOperator(task_id="task3",
                        python_callable=print_hello,
                        provide_context=True,
                        op_kwargs= {'msg' : "Hello task 3"})
    
    t4 = PythonOperator(task_id="task4",
                        python_callable=print_hello,
                        provide_context=True,
                        op_kwargs= {'msg' : "Hello task 4"})
    
    t1.set_downstream(t2)
    t2 >> [t3, t4]

t1
