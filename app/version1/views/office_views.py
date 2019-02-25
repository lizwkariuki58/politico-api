from flask import Blueprint,jsonify,request,make_response
import json
from app.version1.models.models import GovernmentOffice,offices

offices_bp= Blueprint('offices',__name__)

@offices_bp.route('/offices',methods=['POST'])
def create_office():
    data = request.get_json()
    if not request.json:
        return make_response(jsonify({
                'status': 400,
                'error': 'Bad Request, Input all your data in JSON format.'
        }),400)
    
    if len(data['name']) == 0 or len(data['office_type'])==0:
        return make_response(jsonify({
                'Status': 400,
                'Error':'Bad Request, Update all fields of your JSON data'
        }),400)
    
    for office in offices:
        if office.name == data['name']:
            return make_response(jsonify({
                    'status': 409,
                    'error': 'Office already exists'
            }),409)

    new=GovernmentOffice(**data)

    #The new party is added to the parties list. It is then made json serializable
    offices.append(new)
    new_dict = new.__dict__
    return make_response(jsonify({
            'status': 201,
            'Office': new_dict

    }),201)

@offices_bp.route('/offices', methods = ['GET'])
def get_all_offices():
    return make_response(jsonify({
        'Status':200,
        'Offices': offices
    }))

@offices_bp.route('/offices/<int:office_id>', methods = ['GET'])
def get_specific_office(office_id):
    for my_office in offices:
        if my_office['id']==office_id:
            new_dict=my_office.__dict__
            return make_response(jsonify({
                    'Status':200,
                    'Office': new_dict
            }))
    return make_response(jsonify({
        'Status':404,
        'Error': 'Office not found.'
        }))    
