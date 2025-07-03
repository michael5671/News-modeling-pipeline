from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "dataengineer",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "vnexpress_rss_ingest",
    default_args=default_args,
    description="Crawl VnExpress multi-category RSS feeds",
    schedule_interval="0 * * * *",  # chạy mỗi giờ
    start_date=datetime(2025, 7, 2),
    catchup=False,
) as dag:

    crawl_rss = BashOperator(
        task_id="crawl_rss",
        bash_command="python /opt/airflow/scripts/crawl_vnexpress_rss.py"
    )
