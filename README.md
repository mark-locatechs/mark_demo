# Mark Demo

Demo Project from Mark Long (mark@locatechs.com)

## Description

This Demo shows a micro-service structured website. Everything is dockerized and can go to any cloud provider with minimum setup.

- Django frontend node handles static pages and user authentication.
- Flask backend node as micro-service handles data process.

It can be used as a base image for future developments. Frontend node or backend node can be use alone for small sized projects.

### Backend

Flask, Pytest, uWsgi, nginx, supervisord

### Frontend

Django, Bootstrap, Vuejs, uWsgi, nginx, supervisord

## Technologies

- Docker: Containers can be ran anywhere
- Django, Bootstrap, Vuejs: Handles frontend interactions
- Flask, SQLAlchemy: Rest-ful api handles backend traffic
- Mysql(Mariadb): One of the most popular database server
- Marshmallow: Backend data validation
- Pytest: Acceptance test for api
- uWSGI, nginx, suervisord: Ensure fast multi-threaded data handling

## Website Details

bootstrap 4 frontend, with form and modal

form validation frontend and backend

automatic backend pytest, acceptance test for all CRUD api

## Run Guide

### build containers

`docker-compose build`

### start all service

`docker-compose up` , add `-d` for detached mode. Open a new Terminal for following steps if detached mode not used.

### init database, website is fully functional after this point

`docker-compose exec db bash -c 'mysql -udemo -pdemo demo < /db/init.sql'`

### run test, make sure all service started first

`docker-compose exec flask_project pytest -s --disable-pytest-warnings -v tests`

## What next

- in-code comments
- separate config files, can use consul
