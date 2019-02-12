import os

<<<<<<< HEAD
from flask import jsonify,abort, make_response

=======
>>>>>>> ft-get-all-parties-163710397
from app import create_app
from app.version1.views import parties_bp

config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)
<<<<<<< HEAD
=======
app.register_blueprint(parties_bp)

>>>>>>> ft-get-all-parties-163710397
if __name__ == '__main__':
    app.run()