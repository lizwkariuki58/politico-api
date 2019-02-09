from flask import jsonify,abort, make_response
import os
from app import create_app

config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)
parties=[]
parties.append({})
@app.route('/app/version1/parties', methods = ['GET'])
def get_parties():
    return jsonify({'parties': parties})

@app.route('/app/version1/parties/<int:party_id>',methods=['GET'])
def get_party(party_id):
    party = [party for party in parties if party['id'] == party_id]
    if len(party) == 0:
        abort(404)
    return jsonify({'party': party[0]})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),404)
if __name__ == '__main__':
    app.run()