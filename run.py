#this is the application's entry point

import os

from app import create_app

# lets get our FLASK_CONFIG env var on the host, this is set from our docker compose file
config_name = os.getenv('FLASK_CONFIG')

app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
