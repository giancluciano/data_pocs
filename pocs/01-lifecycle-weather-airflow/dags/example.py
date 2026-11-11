from datetime import datetime, timedelta
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator



with DAG(
        "my_tutorial",
        schedule=timedelta(days=1),
        start_date=datetime(2021,1,1)
    ) as dag:
    t1 = BashOperator(task_id="print_date", bash_command="date")

