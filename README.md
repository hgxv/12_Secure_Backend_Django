# Secure Backend Project with Django Rest Framework

This project aims to develop a secure backend architecture using Django Rest Framework (DRF) and PostgreSQL as the database. This README will guide you through the necessary steps to set up the development environment and successfully launch the project.
Prerequisites

Before getting started, make sure you have the following installed on your system:

    Python 3.x
    pip (Python package manager)
    virtualenv (for creating an isolated virtual environment)
    PostgreSQL (https://www.postgresql.org/download/)

# Installation

Clone the project from the Git repository:


    git clone https://github.com/hgxv/12_Secure_Backend_Django.git
    cd EpicEvents

Create a virtual environment:

# Create a virtual environment named 'env'
    py -m venv env

# Activate the virtual environment
Windows

    env\scripts\activate

Linux

    source env/bin/activate

Install project dependencies:

    py -m pip install -r requirements.txt

# PostgreSQL Database Configuration

Create a PostgreSQL database:
    Ensure PostgreSQL is installed and running.
    Create an empty database with a name of your choice (e.g., my_project_db).


Create a .env file at the project's root and configure the database settings as follows:


    DB_NAME='my_project_db'
    DB_USER='username'
    DB_PASSWORD='password'

Be sure to replace username and password with the appropriate authentication information for your database.

# Running the Development Server

Apply initial migrations:

    py manage.py makemigrations
    
    py manage.py migrate

Create a superuser (admin):

    py manage.py createsuperuser

Start the development server:

    py manage.py runserver

The development server will start at http://127.0.0.1:8000/.

Access the admin interface:

Open a web browser and go to the admin interface at http://127.0.0.1:8000/admin/. Use the superuser credentials you created earlier to log in.

