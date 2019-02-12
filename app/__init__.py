import os

from flask import Flask,jsonify
from instance.config import app_config
from app.version1.views import parties_bp

def create_app(config_name):
    app = Flask(__name__, instance_relative_config= True)
    app.config.from_pyfile('config.py')

    app.register_blueprint(parties_bp)

    return app
    
