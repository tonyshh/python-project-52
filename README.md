# Task Manager

[![Actions Status](https://github.com/tonyshh/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/tonyshh/python-project-52/actions)



This is a task management system. <br>
Plan, organize, and collaborate on any project with task management that will fit every need. <br>
Task Manager can **set tasks**, change their **statuses** and **assign responsibility**. <br>
**Log in** or **register** to take advantage of all the features.

![Task-manager](https://user-images.githubusercontent.com/87614163/235889951-af73f69f-479f-4663-a55a-4ef839f13355.gif)


[See more demos](https://github.com/tonyshh/python-project-52#demos)



### Requirements

- [python](https://www.python.org/), version 3.9 or higher
- [poetry](https://python-poetry.org/docs/#installation), version 1.0.0 or higher


### Installation

Clone this repo or download it with pip:
```ch
git clone https://github.com/tonyshh/task-manager.git
```
```ch
pip install --user git+https://github.com/tonyshh/task-manager.git
```

Go to the downloaded dir and install dependencies:
```ch
cd task-manager
make install
```

### Create .env file

```ch
nano .env
```
Write down the following environment variables (paste your data):
```ch
SECRET_KEY = 'AnySecretKey'
ACCESS_TOKEN = 'AnyCharactersForAccessToken'
```

### After all package ready to go
Run WSGI server and follow the [link you will see](http://0.0.0.0:8000):
```ch
make start
```
Or you can use django development server:
```ch
make dev
```
//write about DEBUG in settings.py//

### Afterword
This project use //technology list//


### Demos

#### Package setup


#### Usage


**by [tonyshh](https://github.com/tonyshh)**
