import airflow
from airflow import DAG
from datetime import timedelta
from airflow.operators.bash_operator import BashOperator

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email': ['ahmad.sammy.a@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False
}

dag = DAG(
    'create_emr_bash',
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(hours=2),
    schedule_interval=None
)

create_emr_bash = BashOperator(
    task_id='create_emr_bash',
    dag=dag,
    bash_command="s3://sammy-midterm-code/aws_cli_create_emr.sh"
)

create_emr_bash