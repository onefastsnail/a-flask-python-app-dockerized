from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(datetime.now())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')