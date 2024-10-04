# Django Blood Bank Project

This is a Django-based Blood Bank project that is implemented using Django Rest Framework (DRF). The project utilizes JWT authentication and is dockerized with Docker Compose.

## Features

- Django Rest Framework (DRF) for building APIs
- JWT authentication for secure user authentication
- Dockerized setup for easy deployment using Docker Compose

## Installation(without docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/Ehsanmelm/Django-Blood-Bank.git

2. create venv
   ```bash
   python3 -m venv (you venv name)

3. activate venv
   ```bash
   source venv_name/bin/activate

4. migrations
   ```bash
   pytohn3 manage.py makemigrations
   python3 manage.py migrate

5. runserver
   ```bash
   python3 manage.py runsever


## installation(with docker)
    docker-compose up

  - Access the project at http://localhost:8000/


