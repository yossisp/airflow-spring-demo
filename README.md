### About
The repo contains the minimal [Airflow infra](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) + Spring project [project](https://github.com/spring-projects/spring-petclinic) example.
The repo is useful for demo purposes.

### How To Run
1. Init Airflow db: `docker compose up airflow-init`.
2. Start Airflow: `docker compose up -d`. It will take a few minutes until it's ready. 
3. Run the Spring directly project on your machine (useful for experimenting/making quick code changes):
    1. `cd ./java/spring-petclinic`
    2. `./mvnw spring-boot:run`. Now Spring Boot application is running on port `8081`.
4. Log in Airflow UI: `localhost:8080`. Username and password are `airflow`.
5. Find `pet_clinic_flow_simple` or `tenant_{tenant_id}_daily_workflow` DAGs and run them manually if necessary.