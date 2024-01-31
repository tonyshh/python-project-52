install:
	poetry install

dev:
	python manage.py runserver

PORT ?= 8000
start:
	python manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	python manage.py shell

makemig:
	poetry run python manage.py makemigrations

mig:
	poetry run python manage.py migrate

parsetrans:
	django-admin makemessages --ignore="static" --ignore=".env"  -l ru

trans:
	django-admin compilemessages

lint:
	poetry run flake8 --ignore=E501 task_manager

tests:
	poetry run python manage.py test

tests-cov:
	poetry run coverage run ./manage.py test
	poetry run coverage xml

setup:
	poetry install
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi