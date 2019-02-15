from flask import Blueprint,jsonify,request,make_response, abort
import json
from app.version1.models import GovernmentOffice

offices_bp= Blueprint('offices',__name__)

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
    #This object is created to be able to access the offices list in the GovernmentOffice class
    new= GovernmentOffice()
    new_dict = new.__dict__
    return make_response(jsonify({
        'Offices': new_dict,
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
