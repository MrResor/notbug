# Task 2.1

Create Flask app which will be REST API app for To-Do list, which allow
user to create task, list, update and delete them. Data could be “mocked”, extra
points for using SQLite or PostgreSQL. URLS need to be in REST API
convention.

# Setup

Container can be build and run using the following two commands:
```
sudo docker build -t python_api:latest .
sudo docker run -d --name python_api -p 5001:5000 python_api:latest
```

Port 5001 was used for convenience as api is available under http://141.144.255.102:5001 for testing.

NOTE: since the app is available on the internet at all times, before verification please call http://141.144.255.102:5001/mock,
it will reset app to the initial state.

# Description

Total of 3 endpoints are available in the app

* /mock - resets database to the initial state

* /tasks - GET request returns a list of all tasks, POST requests pushes a new task to the list, payload with "task" and "done" are needed

* /tasks/<task_id> - GET request returns task with given task_id, DELETE will remove that task, and PUT will update it.