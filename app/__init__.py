import os

from flask import Flask
from instance.config import app_config
from app.version1.views.party_views import parties_bp
from app.version1.views.office_views import offices_bp
from app.version2.views.office_view import offices_bp_v2

def create_app(config_name):
    app = Flask(__name__, instance_relative_config= True)
    app.config.from_pyfile('config.py')

    app.register_blueprint(parties_bp, url_prefix='/api/v1/')
    app.register_blueprint(offices_bp, url_prefix = '/api/v1/')
    app.register_blueprint(offices_bp_v2,url_prefix='/api/v2')

    return app
    
