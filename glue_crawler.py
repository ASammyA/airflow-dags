# import boto3

# DEFAULT_ARGS = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': airflow.utils.dates.days_ago(0),
#     'email': ['ahmad.sammy.a@gmail.com'],
#     'email_on_failure': True,
#     'email_on_retry': False
# }

# dag = DAG(
#     'emr_job_flow_manual_steps_dag_pyspark',
#     default_args=DEFAULT_ARGS,
#     dagrun_timeout=timedelta(hours=2),
#     schedule_interval=None
# )

# session=boto3.client('emr','us-east-1')
# def create_glue_crawler(): 

# glue_crawler = AwsGlueCrawlerOperator(
#     task_id='glue_crawler',
#     dag=dag
# )

# glue_crawler