import os

from app import create_app
from app.version1.views import parties_bp

config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)
app.register_blueprint(parties_bp)

if __name__ == '__main__':
    app.run()