"""
Main application file
"""

# third-party imports
from flask import Flask

# local imports
from .config.db import db, mysql
from .config.routes import api_host

def create_app(config):
    app = Flask(__name__)
    # load configurations
    app.config.from_object(config)

    # initialize db database
    db.init_app(app)

    # initialize mysql database
    mysql.init_app(app)

    # initialize api app
    app.register_blueprint(api_host, url_prefix='/api')

    return app
