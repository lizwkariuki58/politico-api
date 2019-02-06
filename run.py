from flask import jsonify
import os
from app import create_app

config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)

parties =[
    {'id':1,
    'name': 'Gryffindor',
    'hqAddress': '4 Privet Drive',
    'logo_url': 'gryffindor.com/logo'},

    {'id':2,
    'name': 'Slytherin',
    'hqAddress': '13 Spinners End',
    'logo_url': 'slytherin.com/logo'},

]
@app.route('/', methods = ['GET'])
def get_parties():
    return jsonify({'parties': parties})

if __name__ == '__main__':
    app.run()