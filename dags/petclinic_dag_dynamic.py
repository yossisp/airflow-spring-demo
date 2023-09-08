from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.http_operator import SimpleHttpOperator

# Define a function to create a DAG for a specific tenant
def create_tenant_dag(tenant_id):
    default_args = {
        'owner': 'your_name',
        'start_date': datetime(2023, 9, 8),
        'retries': 1,  # Number of retries for each task
        'retry_delay': timedelta(seconds=5),  # Delay between retries
        # Define other DAG parameters as needed
    }

    dag = DAG(
        f'tenant_{tenant_id}_daily_workflow',
        default_args=default_args,
        schedule_interval=timedelta(days=1),  # Set the daily schedule
        catchup=False,  # Prevent backfilling for past dates
    )

    show_vets_task = SimpleHttpOperator(
        task_id=f'show_vets_{tenant_id}',
        http_conn_id='pet_clinic_conn',  # Specify your HTTP connection ID
        method='GET',  # HTTP method (e.g., POST)
        endpoint='vets',  # API endpoint URL
        # headers={"Content-Type": "application/json"},  # Specify headers as needed
        # data='{"payload_key": "payload_value"}',  # Specify request data as needed
        dag=dag,
    )

    show_owners_task = SimpleHttpOperator(
        task_id=f'show_owners_{tenant_id}',
        http_conn_id='pet_clinic_conn',  # Specify your HTTP connection ID
        method='GET',  # HTTP method (e.g., POST)
        endpoint='owners',  # API endpoint URL
        # headers={"Content-Type": "application/json"},  # Specify headers as needed
        # data='{"payload_key": "payload_value"}',  # Specify request data as needed
        dag=dag,
    )

    show_vets_task >> show_owners_task

    return dag

# List of tenant identifiers
tenants = ['tenant1', 'tenant2', 'tenant3']

# Generate a separate DAG instance for each tenant
for tenant_id in tenants:
    print(f'generating dag for tenant {tenant_id}')
    globals()[tenant_id] = create_tenant_dag(tenant_id)
    
    