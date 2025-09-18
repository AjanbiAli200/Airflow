from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["xcom-test"]
)
def xcom_s3_test():
    @task()
    def push_xcom(ti=None):
        large_value = 'x' * 1000000  # 1MB string
        ti.xcom_push(key='large_test', value=large_value)
        print('Pushed large XCom value.')
        return large_value

    @task()
    def pull_xcom(ti=None):
        value = ti.xcom_pull(key='large_test', task_ids='push_xcom')
        print(f'Pulled XCom value of length: {len(value) if value else 0}')

    push_xcom() >> pull_xcom()

xcom_s3_test()
