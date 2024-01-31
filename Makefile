dev:
	poetry run python3 manage.py runserver

start:
	python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:8000 task_manager.wsgi

install:
	poetry install

lint:
	flake8 task_manager

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml
