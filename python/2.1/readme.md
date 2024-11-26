# Task 2.1

Create Flask app which will be REST API app for To-Do list, which allow
user to create task, list, update and delete them. Data could be “mocked”, extra
points for using SQLite or PostgreSQL. URLS need to be in REST API
convention.

# Setup

sudo docker build -t python_api:latest .
sudo docker run -d --name python_api -p 5001:5000 python_api:latest