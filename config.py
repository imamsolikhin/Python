"""
Configuration file for the application.
"""

#local import
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
    SECRET_KEY = "b'\x9c\xf5\xba\xd2Q\x9aP\x17\x8b\x8e9\xae5$\x08\xa0'"#os.environ['SECRET_KEY']

    DB_USERNAME = "mrpuser"#os.environ['MYSQL_USER']
    DB_PASSWORD = "admin"#os.environ['MYSQL_PASSWORD']
    DB_HOST = "127.0.0.1"#172.16.26.16#os.environ['MYSQL_HOST']
    DB_NAME = "noc_rml_ikb"#os.environ['MYSQL_DATABASE']
    DB_PORT = 3306#os.environ['MYSQL_PORT']
    DB_URI = "mysql://%s:%s@%s:%s/%s"  % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = DB_URI

    MYSQL_USER = "mrpuser"#os.environ['MYSQL_USER']
    MYSQL_PASSWORD = "admin"#os.environ['MYSQL_PASSWORD']
    MYSQL_HOST = "127.0.0.1"#os.environ['MYSQL_HOST']
    MYSQL_DATABASE = "noc_rml_ikb"#os.environ['MYSQL_DATABASE']
    MYSQL_DB = "noc_rml_ikb"#os.environ['MYSQL_DATABASE']
    MYSQL_PORT = 3306#os.environ['MYSQL_PORT']
    # MYSQL_URI = "mysql://%s:%s@%s:%s/%s" % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
    # MYSQL_DB_HOST = MYSQL_URI

class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class StagingConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
