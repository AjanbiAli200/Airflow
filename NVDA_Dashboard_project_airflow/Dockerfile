FROM quay.io/astronomer/astro-runtime:12.9.0

# Install dependencies from requirements.txt
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy your project files
COPY dags/ /opt/airflow/dags/
COPY plugins/ /opt/airflow/plugins/
COPY include/ /opt/airflow/include/
COPY airflow_settings.yaml /opt/airflow/airflow_settings.yaml
COPY airflow.cfg /opt/airflow/airflow.cfg

# Set user for security
USER astro