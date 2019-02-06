from flask import jsonify,abort
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
@app.route('/app/version1/parties', methods = ['GET'])
def get_parties():
    return jsonify({'parties': parties})

@app.route('/app/version1/parties/<int:party_id>',methods=['GET'])
def get_party(party_id):
    party = [party for party in parties if party['id'] == party_id]
    if len(party) == 0:
        abort(404)
    return jsonify({'party': party[0]})

if __name__ == '__main__':
    app.run()