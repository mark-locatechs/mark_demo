# Mark Demo

Demo Project from Mark Long (mark@locatechs.com)

## Backend

Docker, Flask, Mysql, Pytest, uWsgi, nginx, supervisord

## Frontend

Bootstrap, Vuejs

## Description

The main purpose of this project is a Demo.
It is designed to balance fast development, easy to maintain, portability and scalablity of the application.

## Run Guide

### build containers

`docker-compose build`

### start all service

`docker-compose up` , add `-d` for detached mode, open a new ternimal for following steps if deteached mode not used.

### init database, website is fully functional after this point

`docker-compose exec db bash -c 'mysql -udemo -pdemo demo < /db/init.sql'`

### run test, make sure all service started first

`docker-compose exec flask_project pytest -s --disable-pytest-warnings -v tests`

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

## What next

- in-code comments
- separate config files, can use consul
