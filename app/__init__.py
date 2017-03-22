from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config
import MySQLdb

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():

    	# Open database connection
    	db = MySQLdb.connect("mysql","onefastpython","pass","app" )

    	# prepare a cursor object using cursor() method
    	cursor = db.cursor()

    	# execute SQL query using execute() method.
    	cursor.execute("SELECT VERSION()")

    	# Fetch a single row using fetchone() method.
    	data = cursor.fetchone()

    	# disconnect from server
    	db.close()

        return data


    return app