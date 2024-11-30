## Airflow ETL Pipeline with PostgreSQL and NASA API Integration
## **Project Overview**
This project demonstrates the creation of an ETL (Extract, Transform, Load) pipeline using Apache Airflow, designed to pull data from NASA's Astronomy Picture of the Day (APOD) API, transform it, and load the processed data into a PostgreSQL database. The entire workflow is orchestrated and scheduled by Airflow, ensuring seamless, repeatable, and automated task execution.

The project uses Docker to create isolated and reproducible environments for both Airflow and PostgreSQL services, which ensures a consistent setup across different machines or platforms.

**Key Components**
Airflow: Orchestrates the ETL pipeline, defining, scheduling, and monitoring task execution. Airflow’s Directed Acyclic Graph (DAG) framework is used to manage the dependencies between tasks and handle execution order.
PostgreSQL: The data storage layer for the transformed data. It is hosted in a Docker container and connected to Airflow via hooks and operators.
NASA APOD API: The external data source, providing daily astronomy-related content such as images and metadata, which is processed and stored in PostgreSQL for future analysis and visualization.
**Objective of the Project**
1. Extract Data
The pipeline extracts data from NASA’s Astronomy Picture of the Day (APOD) API on a scheduled basis. The data includes metadata about the daily astronomy image, such as the title, explanation, and URL.

2. Transform Data
Once extracted, the data is processed and transformed to ensure it’s in the correct format for storage in the database. This involves filtering relevant fields like the title, explanation, image URL, and date.

3. Load Data into PostgreSQL
The transformed data is then loaded into a PostgreSQL database. This structured data can be used for future analysis, reporting, or visualization.

**Architecture and Workflow**
The ETL pipeline is orchestrated using Airflow with the following stages:

Extract:
The SimpleHttpOperator in Airflow makes HTTP GET requests to NASA's APOD API. The API returns a JSON response containing fields such as the title, explanation, and URL of the image.

Transform:
The extracted JSON data is processed using Airflow's TaskFlow API. During this stage, relevant fields like the title, explanation, image URL, and date are extracted and formatted to match the structure of the target PostgreSQL database.

Load:
The transformed data is loaded into a PostgreSQL database using PostgreHook and PostgreSQLOperator in Airflow. If the target table doesn’t already exist in the database, it is automatically created as part of the DAG.

**Project Components**
1. Apache Airflow
Airflow is used to define the ETL pipeline and orchestrate the tasks. The workflow is defined in a DAG (Directed Acyclic Graph) which consists of several tasks:

Data extraction using SimpleHttpOperator for interacting with the APOD API.
Data transformation using Airflow's TaskFlow API to parse and clean the data.
Data loading into PostgreSQL using PostgreHook and PostgreOperator.
2. PostgreSQL
PostgreSQL is used as the data storage system for the processed APOD data. The database is hosted in a Docker container to simplify setup and ensure data persistence. The connection between Airflow and PostgreSQL is managed using Airflow’s PostgreHook and PostgreSQLOperator.

3. Docker
Docker is used to containerize the Airflow and PostgreSQL services. This provides a fully isolated environment that ensures the application is portable and reproducible across various platforms. Docker volumes are used to persist PostgreSQL data between container restarts.

4. NASA APOD API
The project interacts with NASA’s Astronomy Picture of the Day API, which provides metadata for a daily astronomy image. The API response contains information such as:

Title of the picture
Explanation of the image
URL to the image
Project Workflow (ETL Process)
1. Extract:
The SimpleHttpOperator in Airflow is used to send HTTP GET requests to NASA’s APOD API.
The API returns a JSON response containing metadata like the title, explanation, and image URL.
Example response from the API:
json
Copy code
{
  "title": "Astronomy Picture of the Day",
  "explanation": "A description of the picture.",
  "url": "http://example.com/image.jpg",
  "date": "2024-11-08"
}
2. Transform:
The JSON response is processed and transformed using Airflow's TaskFlow API.
The relevant fields (title, explanation, URL, and date) are extracted and formatted.
This step ensures that the data is cleaned and ready to be loaded into the PostgreSQL database.
3. Load:
The transformed data is loaded into a PostgreSQL table.
If the table does not already exist, it is created automatically as part of the DAG using a Create Table task.
The data can then be used for analysis, reporting, or visualization.
How to Run the Project
Prerequisites:
Docker: Ensure Docker is installed and running on your machine.
Python 3.x: The project uses Python for Airflow's execution.
PostgreSQL: The database service runs within a Docker container.
Steps to Run the Project:
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/airflow-etl-pipeline.git
cd airflow-etl-pipeline
Build and start Docker containers: The project uses Docker Compose to manage both Airflow and PostgreSQL containers.

bash
Copy code
docker-compose up --build
Access the Airflow Web UI: Once the containers are up and running, access the Airflow web UI at:

bash
Copy code
http://localhost:8080
The default login is admin for both the username and password.

Run the ETL Pipeline: The Airflow DAG will automatically execute based on the scheduled interval (e.g., daily) and will extract data from the NASA API, transform it, and load it into the PostgreSQL database.

Technologies Used
Apache Airflow: Workflow orchestration tool for defining, scheduling, and monitoring the ETL pipeline.
PostgreSQL: Relational database to store the transformed data.
Docker: Containerization platform for creating isolated environments.
NASA APOD API: External API providing daily astronomy content.
Python: Programming language for writing Airflow tasks and defining the DAG.