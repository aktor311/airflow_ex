from datetime import datetime
from airflow.models import DAG
from airflow.hooks.base_hook import BaseHook
from airflow.operators.bash import BashOperator
from utils.check_table_sensor import CheckTableSensor

connection = BaseHook.get_connection("main_postgresql_connection")

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2024, 10, 29),
}

dag = DAG('dag_sensor', default_args=default_args, schedule_interval='0 * * * *', catchup=True,
          max_active_tasks=3, max_active_runs=1, tags=["Fourth dag", "Test"])

task1 = BashOperator(
    task_id='task1',
    bash_command='python3 /airflow/scripts/dag_sensor/task1.py',
    dag=dag)

task_check_table_sensor = CheckTableSensor(
    task_id=f'task_check_table_sensor',
    timeout=1000,
    mode='reschedule',
    poke_interval=10,
    conn=connection,
    table_name='currency2',
    dag=dag
)

task3 = BashOperator(
    task_id='task3',
    bash_command='python3 /airflow/scripts/dag_sensor/task3.py',
    dag=dag)

for i in [1, 2, 3, 4, 5]:
    some_task = BashOperator(
        task_id=f'task4_{str(i)}',
        bash_command='python3 /airflow/scripts/dag_sensor/task1.py',
        dag=dag)
    task3 >> some_task

task1 >> task_check_table_sensor >> task3