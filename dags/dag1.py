from datetime import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2024, 10, 13),
    #"retry_delay": timedelta(minutes=0.1)
}

dag = DAG('dag1', default_args=default_args, schedule_interval='0 23 * * *', catchup=True,
          max_active_tasks=3, max_active_runs=1, tags=["Test", "My first dag"])

task1 = BashOperator(
    task_id='task1',
    bash_command='python3 /airflow/scripts/dag1/task1.py',
    dag=dag)

task2 = BashOperator(
    task_id='task2',
    bash_command='python3 /airflow/scripts/dag1/task2.py',
    dag=dag)

