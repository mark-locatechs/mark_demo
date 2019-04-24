from flask import Flask
import mysql.connector
import simplejson as json
import string
import random

from flask_sqlalchemy import SQLAlchemy

from flask_restful import reqparse, abort, Api, Resource


# config = {
#         'user': 'mysql',
#         'password': 'mysql',
#         'host': 'db',
#         'port': '3306',
#         'database': 'test'
#     }
# connection = mysql.connector.connect(**config)
# cursor = connection.cursor()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://mysql:mysql@db/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

#
# A decorator to manage database connection automatically
#
# def db_connection(func):
#     def function_wrapper(*args, **kwargs):

#         connection = mysql.connector.connect(**config)
#         cursor = connection.cursor()     

#         result = func(*args, **kwargs)

#         cursor.close()
#         connection.close()
#         return result
        
#     return function_wrapper


#
#   CRUD for a single user
#


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/')
def index():
    result = [(user.id, user.name) for user in User.query.all()]

    return json.dumps(result)




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
