# uSmart Flask Application

This repository contains a Flask application developed for the uSmart platform. The application provides a web API to consume data from a CSV file, perform outlier detection on the data, and store it in an SQL database. It utilizes Python and Flask for the backend implementation.

## Project Structure

The project has the following structure:

usmart/
├── app/
│   ├── __init__.py
│   └── views.py
├── config/
│   └── dev_configurations.ini
├── test/
│   ├── test1.csv
│   ├── test2.csv
│   └── test.py
├── Dockerfile
├── docker-compose.yml
├── main.py
├── README.md
└── requirements.txt


- The `app/` directory contains the Flask application code.
  - `__init__.py`: Initializes the Flask application.
  - `views.py`: Defines the API endpoints and request handlers.

- The `config/` directory contains the configuration file.
  - `dev_configurations.ini`: Contains the database configurations.

- `Dockerfile`: Specifies the Docker image configuration for running the application.
- `docker-compose.yml`: Defines the services and their configurations for Docker Compose.
- `main.py`: Entry point of the application.
- `README.md`: This file providing an overview of the project.
- `requirements.txt`: Lists the required Python dependencies for the project.

## Getting Started

To set up and run the application locally, follow these steps:

1. Clone this repository:

   git clone https://github.com/4ashapriya/usmart
   cd usmart

2. Install the required dependencies using pip:

pip install -r requirements.txt

3. Configure the database connection:

Open the config/dev_configurations.ini file.
Update the database host, port, dbname, user, and password as per your environment.
4. Run the application:

python main.py

5. Once the application is running, you can make API requests to consume data from a CSV file, perform outlier detection, and store it in the configured SQL database.

## Docker Support
This application can also be run using Docker and Docker Compose. Docker provides a consistent and reproducible environment for the application.

To run the application using Docker, follow these steps:

1. Ensure Docker is installed on your system.

2. Build the Docker image:

docker build -t usmart-app .

3. Start the application using Docker Compose:

docker-compose up

This will start the application along with the necessary services (e.g., PostgreSQL).

4. The application will be accessible at http://localhost:5000.