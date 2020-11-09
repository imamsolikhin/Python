"""
Command for running the application
"""
# from flask import Flask

# local imports
from config import DevelopmentConfig, ProductionConfig, StagingConfig

from app import create_app
import os

# main entry point of the app
app = create_app(ProductionConfig)


if __name__ == '__main__':
    app.run()
