from flask import Blueprint, json,jsonify,request,make_response

from app.version1.models import PoliticalParty

parties_bp= Blueprint('parties',__name__)

@parties_bp.route('/parties', methods = ['POST'])
def create_party():
    party= PoliticalParty()
    details = request.get_json()
    name = details['name']
    hqAddress = details['hqAddress']
    slogan = details['slogan']

    new_party = {
        'id' : len(party.parties)+1,
        'name': name,
        'hqAddress': hqAddress,
        'slogan':slogan
    }   

    party.parties.append(new_party) 
    return make_response(jsonify({
        'Message': 'Party created successfully',
        'Party Name': new_party['name']
    }))

@parties_bp.route('/parties', methods = ['GET'])
def get_all_parties():
    party= PoliticalParty()
    return make_response(jsonify({
        'parties': party.parties,
        'status': 'OK'
    }),200)