#!/usr/bin/env python

from flask import Flask, jsonify, request, abort, Blueprint
from flask_cors import CORS
from flask import render_template


from flask_sqlalchemy import get_debug_queries
from flask_restful import  Api, Resource, fields, marshal, marshal_with

from app.controllers import RouteController, RoutesController, EventsController, EventController, CitiesController
from app.models import database_init
from app.shared import db



app = Flask(__name__)

# only for dev
app.debug = True

# cors
CORS(app)



# init database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://demo:demo@db:3306/demo?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_pre_ping': True}
app.config['SQLALCHEMY_POOL_SIZE'] = 2
app.config['SQLALCHEMY_POOL_RECYCLE'] = 500


db.init_app(app)

# Rest Controller

api_bp = Blueprint('api', __name__)
api = Api(app)



api.add_resource(RoutesController, '/route')
api.add_resource(RouteController, '/route/<int:id>')


api.add_resource(EventsController, '/event')
api.add_resource(EventController, '/event/<int:id>')

api.add_resource(CitiesController, '/city')

app.register_blueprint(api_bp)


#Enable when needed...
# def sql_debug(response):
#     queries = list(get_debug_queries())
#     for q in queries:
#         stmt = str(q.statement % q.parameters)
#         print(stmt)

#     return response

# app.after_request(sql_debug)
