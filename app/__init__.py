import os

from flask import Flask,jsonify
from instance.config import app_config
from app.version1.views.party_views import parties_bp
from app.version1.views.office_views import offices_bp

def create_app(config_name):
    app = Flask(__name__, instance_relative_config= True)
    app.config.from_pyfile('config.py')

    app.register_blueprint(parties_bp, url_prefix='/api/v1/')
    app.register_blueprint(offices_bp, url_prefix = '/api/v1/')

    return app
    
