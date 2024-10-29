from datetime import datetime
from airflow.models import DAG
from airflow.hooks.base_hook import BaseHook
from dag3_plugin.dag3_operator import MyFirstExOperator

connection = BaseHook.get_connection("main_postgresql_connection")

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2024, 10, 29),
}

dag = DAG('dag3', default_args=default_args, schedule_interval='0 * * * *', catchup=True,
          max_active_tasks=3, max_active_runs=1, tags=["Third dag", "Test"])

task1 = MyFirstExOperator(
    task_id='task1',
    postgre_conn=connection,
    currency='EUR',
    value=99.0,
    dag=dag)

task2 = MyFirstExOperator(
    task_id='task2',
    postgre_conn=connection,
    currency='RUB',
    value=1.0,
    dag=dag)

task1 >> task2