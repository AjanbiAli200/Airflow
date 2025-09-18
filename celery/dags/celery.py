from airflow.decorators import dag, task
from pendulum import datetime
from time import sleep

@dag(start_date=datetime(2025, 1, 1), schedule=None, catchup=False)
def celery():
    
    @task(queue="cpu")
    def a():
        print("Task A")
        sleep(15)

    @task(queue="gpu")
    def b():
        print("Task B")
        sleep(15)

    @task(queue="cpu")
    def c():
        print("Task C")
        sleep(15)

    @task(queue="cpu")
    def d():
        print("Task D")
        sleep(15)
        
    @task
    def e():
        print("Task E")
        sleep(15)
        
    a() >> [b(), c(), d()] >> e()
    
celery()