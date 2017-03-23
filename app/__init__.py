from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask.json import jsonify
import MySQLdb

# Import classes from your brand new package
from Bikes import Mtb
from Bikes import Bmx

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

    @app.route('/bikes')
    def bikes():

    	# Create an object of Mtb class
    	myMtb = Mtb()
    	myBmx = Bmx()

    	merge = myMtb.brands + myBmx.brands

    	merge.sort()

    	return jsonify(merge)

    return app