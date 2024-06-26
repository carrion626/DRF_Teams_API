# Team Management REST API DRF
REST API with CRUD endpoints for teams and people

Python 3.9.13

# Description:
- Object Team with "name"
- Object People with "name", "surname", "email"
- People and teams can be created, edited and deleted, People can be assigned to the team


# How to install:
- Create directory where you want to store project.
- Console "git clone https://github.com/carrion626/DRF_Teams_API.git"
- Create venv
- Install requirements
- Console: "python manage.py makemigrations" "python manage.py migrate" for migrations
- Console: "python manage.py runserver" to run project

If localhost: "http://localhost:8000/api/"

You can test it with Postman now:

- Create - POST http://localhost:8000/api/teams/ or http://localhost:8000/api/people/

{"name": "Engineering Team"} - for team 

{
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "team": 1
} - for person

- Update - PUT http://localhost:8000/api/teams/1/ or http://localhost:8000/api/people/1/
- Delete - DELETE http://localhost:8000/api/teams/1/ or http://localhost:8000/api/people/1/