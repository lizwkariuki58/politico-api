import os

from flask import jsonify,abort, make_response

from app import create_app
from app.version1.views.party_views import parties_bp
from app.version1.views.office_views import offices_bp

#Create app using create_app method from __init__.py
config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)

#Register blueprints
app.register_blueprint(parties_bp)
app.register_blueprint(offices_bp)

if __name__ == '__main__':
    app.run()