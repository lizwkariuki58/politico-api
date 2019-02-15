from flask import Blueprint,jsonify,request,make_response, abort
import json
from app.version1.models import PoliticalParty, GovernmentOffice

parties_bp= Blueprint('parties',__name__)
offices_bp= Blueprint('offices',__name__)

@parties_bp.route('/parties', methods = ['POST'])
def create_party():
    #This method should only be available to an admin user. 
    #Responses from the request.get_json request saved in a Python dictionary called data.
    data = request.get_json()

    name = data['name']
    hqAddress= data['hqAddress']
    slogan= data['slogan']

     # Instance of PoliticalParty is created and the data above is unpacked as an argument
    new=PoliticalParty(**data)

    #The new party is added to the parties list. It is then made json serializable
    new.parties.append(new)
    new_dict = new.__dict__
    return make_response(jsonify({
            'Party': new_dict,
            'status':'200 OK'

    }))

@parties_bp.route('/parties', methods = ['GET'])
def get_all_parties():
    #This method should be available to all users
    new= PoliticalParty()
    return make_response(jsonify({
        'parties': new.parties,
        'status': '200 OK'
    }),200)

@parties_bp.route('/parties/<int:party_id>', methods = ['GET'])
def get_specific_party(party_id):
    new = PoliticalParty()
    for party in new.parties:
        if new.id==party_id:
            new_dict=new.__dict__
            return make_response(jsonify({
                    'Party':new_dict,
                    'Status':'200 OK'
            }))
    return make_response(jsonify({
        'Message':'Party Not Found',
        'Status': '404 Not Found'
        }))    

@parties_bp.route('/parties/<int:party_id>', methods =['PUT'])
def update_party(party_id):
    new= PoliticalParty()
    data= request.json
    for party in new.parties:
        if new.id==party_id:
            if request.json:
                new.name=data.get('name', new.name)
                new.hqAddress=data['hqAddress']
                new.slogan=data['slogan']
            return make_response(jsonify({
                    'Message':'Party not Updated',
                    'Status':'400 Bad Request'
                    }))
    new_dict=new.__dict__
    return make_response(jsonify({
        'Message':new_dict,
        'status':'200 OK'
    }))
    return make_response(jsonify({
        'Message':'Party Not Found',
        'Status':'404 Party Not Found'
        }))

@parties_bp.route('/parties/<int:party_id>',methods=['DELETE'])
def delete_party(party_id):
    new = PoliticalParty()
    for party in new.parties:
        if new.id==party_id:
            new.parties.remove(new)
            new_dict=new.__dict__
            return make_response(jsonify({
                    'Party':'Party Deleted',
                    'Status':'200 OK'
            }))
    return make_response(jsonify({
        'Message':'Party Not Found',
        'Status': '404 Not Found'
        }))    

@offices_bp.route('/offices',methods=['POST'])
def create_office():
    data = request.get_json()

    office_type = data['office_type']
    name= data['name']

    new=GovernmentOffice(**data)

    new.offices.append(new)
    new_dict = new.__dict__
    return make_response(jsonify({
            'Office': new_dict,
            'status':'200 OK'

    }))

@offices_bp.route('/offices', methods = ['GET'])
def get_all_offices():
    #This method should be available to all users
    new= GovernmentOffice()
    return make_response(jsonify({
        'Offices': new.offices,
        'Status': '200 OK'
    }))

@offices_bp.route('/offices/<int:office_id>', methods = ['GET'])
def get_specific_office(office_id):
    #This object is created to access the office[] list in the Government Offices class
    new = GovernmentOffice()
    for govt_office in new.offices:
        if govt_office.id==office_id:
            govt_office_dict=govt_office.__dict__
            return make_response(jsonify({
                    'Status': 200,
                    'Office': govt_office_dict
            }))
    return make_response(jsonify({
        'Status': '404',
        'Error': 'Office Not Found'
        }))    
