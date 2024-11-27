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

Database holds information in the following format [task id, task name / message, status of the task]. Task id is an integer does not have to be revealed to the user but it is a primary key of the table. Message is a text that is asociated with a task. Lastly, status is an integer of values either 0 or 1, where 0 indcicates that the task has not been done yet and 1 a finished task.

Total of 3 endpoints are available in the app

* /mock

    GET - resets database to the initial state.

* /tasks

    GET - returns a list of all tasks.
    
    POST - pushes a new task to the list, payload with "task" and "done" are needed. Examplary json file below.
   
    ```
    {
        "task": "Examplary task",
        "done": 0
    }
    ```

* /tasks/<task_id>

    NOTE. If there is no task with task_id in the database, any request will return a 404 status code

    GET - returns task with given task_id.
    
    DELETE - remove task with task id equal to the given one.
    
    PUT - update task with the the given task_id. Payload is similar to the /task POST request, but only
    one of the keys is required. In case non of them are given, request will return a 204 status code.