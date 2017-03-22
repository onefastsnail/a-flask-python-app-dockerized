from flask import Flask

# instance_relative_config=True === will load the specified file from the instance/ directory.
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')
