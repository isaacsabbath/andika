#!/bin/bash

# This script sets up the BlogFast Django project by installing dependencies,
# applying migrations, and creating a superuser.
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py tailwindcss install
python manage.py collectstatic --noinput
