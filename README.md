# Mark Demo

Demo Project from Mark Long (mark@locatechs.com)

## Description

This Demo shows a micro-service structured website. Everything is dockerized and can go to any cloud provider with minimum setup.

- Django frontend node handles static pages and user authentication.
- Laravel frontend node doing exactly same thing as Django node.
- Flask backend node as micro-service handles data process.
- Nginx reverse proxy, has separated frontend backend network.

I try to keep system requirements, dependencies as minimum as possible. It can be used as base image for future developments. Frontend node or backend node can be use alone for small sized projects.

### Backend

Flask, Pytest, uWsgi

### Frontend

Django, Bootstrap, Vuejs, uWsgi
Laravel, Bootstrap, Vuejs, php-fpm

## Technologies

- Docker: Containers can go anywhere
- Django, Bootstrap, Vuejs: Handles frontend interactions
- Flask, SQLAlchemy: Micro-service rest-ful CRUD api handles backend traffic
- Mysql(Mariadb): One of the most popular database server
- Marshmallow: Backend data validation
- Pytest: Acceptance test for api
- uWSGI: Ensure fast multi-threaded data handling
- nginx: Act as a reserve proxy, handle ssl, simple load balancing etc.

## Website Detail

![alt text](/images/index.PNG?raw=true "home page")

Website is simple, user can click on `New Route` button to create routes. Each route have a remove button to delete itself.
User can add event to each route, a event must have a start point, a end point and a date. Click the `Create` button will try to create the event. Error with displayed to correspondent field when condition not allowed.

And there is a second page 'lorem' to show user authentication mechanism. Only authenticated user can visit this page. Username and Password are both `demo` here.

- Website uses Bootstrap 4 with modal forms
- Vuejs plugin vuejs-datepicker for date input field
- Axios for asynchronous api calls
- moment for formatting time

## Run Guide

### build containers

`docker-compose build`

### start all service

`docker-compose up` , add `-d` for detached mode. Open a new Terminal for following steps if detached mode not used.

### init database, website is fully functional after this point

`docker-compose exec db bash -c 'mysql -udemo -pdemo demo < /db/init.sql'`

### run test, make sure all service started first

`docker-compose exec flask_project pytest -s --disable-pytest-warnings -v tests`

### Worth to mention

- Remember to run database init code, after all services is stared up and running
- Refresh browser when buttons are inactive, js can be cached, no js versioning right now
- Pytest will reset all stored data

### useful links

- http://localhost:8000/ : django public address
- http://localhost:8001/ : laravel public address

- http://localhost:8010/ : django homepage after proxy
- http://localhost:5000/city : micro-service api
- http://localhost:8080/ : Adminer database GUI, `demo` as username, password and database name
