#this is the application's entry point

import os

from app import create_app

config_name = 'development'
app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
