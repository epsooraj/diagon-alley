venv=venv/bin/python

runserver:
	 $(venv) manage.py runserver

makemigrations:
	 $(venv) manage.py makemigrations

migrate:
	 $(venv) manage.py migrate

