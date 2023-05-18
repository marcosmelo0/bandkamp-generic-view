#!/bin/bash


# Build the project


echo "Building the project..."
python3.9 -m pip install -r requirements.txt


echo "Make Migrations"
python3.11.0 manage.py makemigrations --noinput
python3.11.0pip install wheel setuptools pip --upgrade manage.py migrate --noinput


echo "Collect Static..."
python3.9 manage.py collectstatic --no-input --clear


echo "BUILD END"