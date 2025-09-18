#!/bin/bash
set -e

# Initialize DB
airflow db init

# Start Webserver + Scheduler
airflow webserver -p 8080 &
airflow scheduler
