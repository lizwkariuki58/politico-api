from flask import Blueprint,jsonify,request,make_response, abort
import json
from app.version1.models.models import PoliticalParty, parties

parties_bp= Blueprint('parties',__name__)

@parties_bp.route('/parties', methods = ['POST'])
def create_party():
    
    if not request.json or not 'name' in request.json or not 'hqAddress' in request.json:
        return make_response(jsonify({
                'status': 400,
                'error': 'Bad Request, Update your JSON data.'
        }))
    
    data = request.get_json()

    for party in parties:
        if party['name'] == data['name']:
            return make_response(jsonify({
                    'status': 409,
                    'error': 'Party already exists'
            }))

    name = data['name']
    hqAddress= data['hqAddress']
    slogan= data['slogan']

    new=PoliticalParty(**data)

    #The new party is added to the parties list. It is then made json serializable
    parties.append(new)
    new_dict = new.__dict__
    return make_response(jsonify({
            'status': 201,
            'Party': new_dict

    }))

@parties_bp.route('/parties/', methods = ['GET'])
def get_all_parties():
    #This method should be available to all users
    return make_response(jsonify({
        'status':200,
        'Parties': parties
    }))

@parties_bp.route('/parties/<int:party_id>', methods = ['GET'])
def get_specific_party(party_id):
    for my_party in parties:
        if my_party['id']==party_id:
            new_dict=my_party.__dict__
            return make_response(jsonify({
                    'Status':200,
                    'Party': new_dict
            }))
    return make_response(jsonify({
        'Status':404,
        'Error': 'Party not found.'
        }))    

@parties_bp.route('/parties/<int:party_id>', methods =['PUT'])
def update_party(party_id):
    if not request.json or not 'id' in request.json:
        return make_response(jsonify({
                'status': 400,
                'Error':'Bad Request, Please update your JSON'
        }))
    for my_party in parties:
        if my_party['id']==party_id:
            data = request.json()

            my_party['name']= data['name']
            my_party['hqAddress']= data['hqAddress']
            my_party['slogan']= data['slogan']
            return make_response(jsonify({
                'Status':200,
                'Party': my_party
            }))
    return make_response(jsonify({
            'Status':404,
            'Error': 'Party not found'
    }))

@parties_bp.route('/api/v1/parties/<int:party_id>',methods=['DELETE'])
def delete_party(party_id):
    for my_party in parties:
        if my_party['id']==party_id:
            parties.remove(my_party)
            return make_response(jsonify({
                    'Status':200,
                    'Message': 'Party deleted'
            }))
    return make_response(jsonify({
        'Status': 404,
        'Error':'Party not found'
        }))    
