#!/bin/sh

python manage.py makemigrations job
python manage.py makemigrations note
python manage.py makemigrations photo

python manage.py makemigrations

python manage.py migrate

python init_job_db.py
python init_note_db.py
python init_photo_db.py

python manage.py runserver 0.0.0.0:8000