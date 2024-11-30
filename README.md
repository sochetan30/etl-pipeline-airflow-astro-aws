## Project Overview: Airflow ETL Pipeline with PostgreSQL and NASA API Integration


This project involves creating an ETL pipeline using Airflow. The pipeline extract data from NASA's Astronomy Picture of the Day(APOD) API, transforms the data and loads it into a PostgreSQL databases. The entire workflow is orchestrated by Airflow, a platform that allows scheduling, Monitoring and managing Workflow.

The project leverage Docker to run Airflow and Postgre services, ensuring an isolated and reporducible environment. We also utilize Airflow hooks and operators to handle ETL process efficiently.

Key Components of Airflow for Orchestration:

Airflow is used to define, schedule and monitor the entire the ETL pipeline. It manages task dependecies, ensuring that the process run sequentially and reliably. The Airflow DAG defines the workflow, which include tasks like data extraction, transformation, and loading, postgre database.

A postgresql is used to store the extracted and transformed data. Postgre hosted in docker container, making it easy to manage and ensuring data persistence through docker volumns. We interact with Postgre using AirflowsPostgreHook andn Postgreperators. 

NASA API(A Picture Of The Day):
The External API used in projet. This provides data about the astronomy picture of the day. including metadata like the title, explanation and the URL of the image. We use Airflow's SimpleHttpOperator to extract data fromt he API. Objective of the project : 

**Extract Data:**

The pipeline extracts astronomy related data from the NASA's APOD API on the scheduled basis

**Transform Data:**
Transformations such as filtering or processing the API response are performed to ensure that the is in suitable format before being inserted into the databse.

**Load Data into Postgre:**
The transformed data is loaded into the psql databse the data cab be used further for analysis, reporting or visualization. architecture and workflow. The ETL pipeline is orchestrated in airflow using DAG. 
**The pipeline consists of following stages**

1. Extarct: The SimpleHttpOperator is used to make the HTTP GET requests to NASA's APOD API> The response is in JSON format containing fields like the title of picture, the explanation and the URL of the image.

2. Transform: Extracted JSON is processed in the transform task using airflow TaskFlow API this stage involves extracting relevent fields like title, explanation url and date and ensuring they are in the correct format for the database.

3. Load: Transformed data is loaded into the PSQL table using the PostgreHook If the target table doesnot exist in the postgre ddatabase it is created automatically as parrt of the DAG using create table task.