import os
from datetime import timedelta
from datetime import datetime
from airflow.models import DAG
from airflow.operators.papermill_operator import PapermillOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'Walter',
    'start_date': datetime(2020, 05, 25),
}

with DAG(
    dag_id='COVID_V2',
    default_args=default_args,
    schedule_interval='@daily',
    dagrun_timeout=timedelta(minutes=10),
) as dag:
    # [START howto_operator_papermill]
    run_this = PapermillOperator(
        task_id="COVID_V2_notebook",
        input_nb="/home/ubuntu/COVID/COVID_V_produccion.ipynb",
        output_nb="/home/ubuntu/COVID/out_COVID_V-{{ execution_date }}.ipynb",
        parameters={'msgs': 'Ran from Airflow at {{ execution_date }}!'}
    )
    # [END howto_operator_papermill]