venv=venv/bin/python

runserver:
	 $(venv) manage.py runserver

r: runserver

makemigrations:
	 $(venv) manage.py makemigrations

mm: makemigrations

migrate:
	 $(venv) manage.py migrate

m: migrate

shell:
	 $(venv) manage.py shell_plus

s: shell