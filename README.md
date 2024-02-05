### Hexlet tests and linter status:
[![Actions Status](https://github.com/tonyshh/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tonyshh/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/c30852e1711cc1ed053b/maintainability)](https://codeclimate.com/github/tonyshh/python-project-52/maintainability)

# [TASK MANAGER](https://python-project-52-production-c5a7.up.railway.app/)



Plan, organize, and collaborate on any project with task management that will fit every need. Task Manager allows you to set tasks, change their statuses, and assign responsibility. Make your teamwork more efficient and seamless.

## Features

- **User Authentication**: Secure log in and registration to keep your tasks private.
- **Task Management**: Create, update, and delete tasks with ease.
- **Status Updates**: Easily update the progress of tasks with customizable statuses.
- **Responsibility Assignment**: Assign tasks to team members and manage workload distribution.

## Getting Started

### Prerequisites

The app is built with the Django framework and utilizes built-in libraries such as Django admin, Django filters, and Django-bootstrap, as well as other external libraries. Ensure you have all the dependencies installed:

- Python >= 3.8
- Django >= 4.2.2
- and others listed in the requirements section below.

It's hosted on Railway, but if the link doesn't work, you can run the app locally.

### Requirements

Before starting the application, make sure to install the following dependencies:


- python = "^3.8"
- django = "^4.2.2"
- django-admin = "^2.0.2"
- python-dotenv = "^1.0.0"
- dj-database-url = "^2.0.0"

Additionally, set your environment variables for both development and production environments:

- `DATABASE_URL`
- `SECRET_KEY`
- `DEBUG`
- `ROLLBAR_TOKEN` (if using Rollbar)

### Installation

Ensure you have **poetry** installed to utilize commands from the Makefile. Check your current pip version and upgrade if needed:

```bash
python -m pip --version
python -m pip install --upgrade pip
```


Makefile Commands

Use these commands to manage the application:

    make install: Install poetry packages
    make dev: Start the app on the local server in development mode
    make start: Start the app in production mode
    make migrations: Create migrations for your database
    make migrate: Apply database migrations