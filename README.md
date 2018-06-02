MoMo

Description


User Stories

    Sign in with the application to start using.


Setup/Installation Requirements
Prerequisites

    "AN OPEN MIND AND AN EMPTY CUP"
    Python 3.6.2
    Virtual environment
    Postgres Database
    Internet

Installation Process

    Copy repolink
    Run git clone REPO-URL in your terminal
    Write cd vegang
    Create a virtual environment with virtualenv virtual or try python3.6 -m venv virtual
    Create .env file touch .env and add the following:

SECRET_KEY=<your secret key>
DEBUG=True

    Enter your virtual environment source virtual/bin/activate
    Run pip install -r requirements.txt or pip3 install -r requirements.txt
    Create Postgres Database

psql
CREATE DATABASE gram

    Change the database information in momo/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'momo',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}

    Run ./manage.py runserver or python3.6 manage.py runserver to run the application

Known Bugs

No known bugs
Technologies Used

    Python3.6
    Django
    Bootstrap
    Postgres Database
    CSS
    HTML
    Heroku

License

This project is licensed under the MIT License - see the LICENSE.md file for details MIT (c) 2018 Abdullahinur Abdullahi
Acknowledgements

    Moringa School
