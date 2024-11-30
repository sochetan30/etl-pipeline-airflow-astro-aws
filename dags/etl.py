from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json

## Define the DAG

with DAG(
    dag_id='nasa_apod_postgres',
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    ## Step 1: Create the table if it does not exists:
    @task
    def create_table():
        ## Initliaze the postgre hook
        postgres_hook=PostgresHook(postgres_conn_id="my_postgres_connection")

        ## SQL Query to create a table:
        create_table_query="""
        CREATE TABLE IF NOT EXISTS apod_data(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );
        """

        ## Execute teh table creation query
        postgres_hook.run(create_table_query)
        

        ## Step 2: Extract the NASA API data (APOD data) - Extract Pipeline

    extract_apod=SimpleHttpOperator(
        task_id='extract_apod',
        http_conn_id='nasa_api',
        endpoint='planetary/apod',  ## NASA API endpoint
        method='GET',
        data={"api_key":"{{conn.nasa_api.extra_dejson.api_key}}"},
        response_filter=lambda response:response.json() ## Convert response to JSON
        )        
        # api key: https://api.nasa.gov/planetary/apod?api_key=5CZ2RzvhccIfStjeVcPOOJsuIHFLHYgRP6qWSL3O
    ## Step 3: Transform the data(Pick the info that need to be saved)
    @task
    def transform_apod_data(response):
        apod_data={
            'title': response.get('title',''),
            'explanation': response.get('explanation',''),
            'url': response.get('url',''),    
            'date': response.get('date',''),
            'media_type': response.get('media_type','')                    
        }
        return apod_data

    ## Step 4: Load the data into postgre SQL
    @task
    def load_data_to_postgres(apod_data):
        postgres_hook=PostgresHook(postgres_conn_id='my_postgres_connection')

        # Define SQL query
        insert_query="""
        INSERT INTO apod_data (title, explanation, url, date, media_type)
        VALUES (%s,%s,%s,%s,%s)
        """
        
        # Execute the sql query
        postgres_hook.run(insert_query, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type']
        ))



    ## Step 5: Verify the data in DBeaver


    ## Step 6: Define the task dependecies
    create_table() >> extract_apod ## ENsure the table is created before extraction
    api_response=extract_apod.output
    #simple http oerator has vairable as output.

    transform_data=transform_apod_data(api_response)
    
    load_data_to_postgres(transform_data)
    