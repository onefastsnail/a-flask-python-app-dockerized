from flask import render_template
from datetime import datetime

from app import app

@app.route('/')
def index():
    return render_template("index.html", time=str(datetime.now()))


@app.route('/about')
def about():
    return render_template("about.html")
