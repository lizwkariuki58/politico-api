from flask import Blueprint,jsonify,request,make_response,abort
import json
from app.version1.models import PoliticalParty

parties_bp= Blueprint('parties',__name__)

@parties_bp.route('/parties', methods = ['POST'])
def create_party():
    #Responses from the request.get_json request saved in a Python dictionary called data.
    data = request.get_json()

    name = data['name']
    hqAddress= data['hqAddress']
    slogan= data['slogan']

     # Instance of PoliticalParty is created and the data above is unpacked as an argument
    new=PoliticalParty(**data)

    #The new party is added to the parties list. It is then made json serializable
    new.parties.append(new)
    new_dict = json.dumps(new.__dict__)
    return make_response(jsonify({
            'Party': new_dict,
            'status':'OK'

    }))

@parties_bp.route('/parties', methods = ['GET'])
def get_all_parties():
    new= PoliticalParty()
    return make_response(jsonify({
        'parties': new.parties,
        'status': 'OK'
    }),200)
