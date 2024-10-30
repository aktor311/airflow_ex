from datetime import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.models import Variable

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2024, 10, 30),
}

dag = DAG('dag_variables', default_args=default_args, schedule_interval=None, catchup=True,
          max_active_tasks=3, max_active_runs=1, tags=["Test", "Variables"])

v_value = Variable.get("test_variable")
v_password = Variable.get("main_password")

d_values = Variable.get("json_variable", deserialize_json=True)

task1 = BashOperator(
    task_id='task1',
    bash_command='python3 /airflow/scripts/dag_variables/main_script.py --variable ' + v_value,
    dag=dag)

task2 = BashOperator(
    task_id='task2',
    bash_command='python3 /airflow/scripts/dag_variables/main_script.py --variable ' + v_password,
    dag=dag)

for one_value in d_values.get("list_val"):
    some_task = BashOperator(
        task_id=one_value,
        bash_command='python3 /airflow/scripts/dag_variables/main_script.py --variable ' + one_value,
        dag=dag)
    task2 >> some_task

task1 >> task2