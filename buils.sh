# !/bin/bash
# This script is used to build the project

echo "Building the project"
python3.11 -m pip install -r requirements.txt 

echo "Making migrations"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files"
python3 manage.py collectstatic --noinput --clear


