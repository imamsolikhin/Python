"""
Database configuration file for the application.
"""

# third-party imports
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL


db = SQLAlchemy()
mysql = MySQL()
marshmallow = Marshmallow()
