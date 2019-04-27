# Mark Demo
Demo Project from Mark Long (mark@locatechs.com)
## Backend:
Docker, Flask, Mysql, Pytest, uWsgi, nginx, supervisord
## Frontend:
Bootstrap, Vuejs

## Description:
The main purpose of this project is a Demo.
It is designed to balance fast development, easy to maintain, portability and scalablity of the application.

## Run Guide
###### build containers
docker-compose build

###### init database
docker-compose run app python db_init.py

###### start all service
docker-compose up -d

###### run test, make sure all service started first
docker-compose exec app pytest -s --disable-pytest-warnings -v tests


## Technologies
- Docker is chosed for its portablilty and scalable nature.
- Flask, SQLAlchemy is chosed for fast development.
- Pytest for extra security for further development and maintainability
- uWSGI, nginx, suervisord are for stability, multi-thread operation.
- Bootstrap 4 for fast frontend designs
- Vuejs for UX interactions

All above mixed together, i want to a goal to bring up a complete website as fast as possible and not losing

## Details

bootstrap 4 frontend, with form and modal

formvalidation frontend and backend

automatic backend pytest, accpetance test for all CRUD api



## what next:
- separate config files, can use consul
