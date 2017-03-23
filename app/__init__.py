from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask.json import jsonify
from flask import Response
from flask import json
import MySQLdb

# Import classes from your brand new package
from Bikes import Mtb
from Bikes import Bmx
import Posts

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

#this is called from run.py when booting up the app
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)

    from app import models

    #using python decorators to extend functions without modifing them
    @app.route('/')
    def hello_world():

    	# Open database connection
    	db = MySQLdb.connect("mysql","root","pass","app")

    	# prepare a cursor object using cursor() method
    	cursor = db.cursor()

    	# execute SQL query using execute() method.
    	cursor.execute("SELECT VERSION()")

    	# Fetch a single row using fetchone() method.
    	data = cursor.fetchone()

    	# disconnect from server
    	db.close()

    	return data

    @app.errorhandler(404)
    def not_found(error=None):
        message = {
                'status': 404,
                'message': 'Not Found Amigo',
        }
        resp = jsonify(message)
        resp.status_code = 404

        return resp

    @app.route('/users/<userid>', methods = ['GET'])
    def api_users(userid):
        users = {'1':'john', '2':'steve', '3':'bill'}

        if userid in users:
            return jsonify({userid:users[userid]})
        else:
            return not_found()

    @app.route('/hello', methods = ['GET'])
    def api_hello():
        data = {
            'hello'  : 'world',
            'number' : 3
        }

        #Serialize obj to a JSON format #https://docs.python.org/2/library/json.html
        myjson = json.dumps(data)

        resp = Response(myjson, status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://www.onefastsnail.com'

        return resp

    @app.route('/bikes')
    def bikes():

    	# Create an object of Mtb class
    	myMtb = Mtb()
    	myBmx = Bmx()

    	merge = myMtb.brands + myBmx.brands

    	merge.sort()

    	return jsonify(merge)

    @app.route('/posts')
    def posts():

    	posts = Posts.getposts()

    	return jsonify(posts)

    return app