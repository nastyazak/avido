#!bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input
gunicorn djangoProject.wsgi:application --bind 0.0.0.0:8000 --reload