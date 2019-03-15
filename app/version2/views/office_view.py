from flask import Blueprint, request, jsonify, make_response
from app.version2.models.office_model import Office

offices_bp_v2 = Blueprint('officesv2',__name__)
office = Office()

@offices_bp_v2.route('/offices', methods=['POST'])
def post_office():
    if not request.get_json():
        return make_response(jsonify({
            "status":404,
            "error": "Please provide office data in JSON format"
        }),404)
        
    data = request.get_json()
    new_office = {
        "name": data['name'],
        "office_type": data["office_type"]
    }

    office = Office(**new_office)
    office.save()

    return make_response(jsonify({
        "status": 201,
        "message": "Office created,{}".format(office.convert_to_json())
    }),201)

@offices_bp_v2.route('/offices', methods=['GET'])
def get_all_offices():
    all = office.get_all()
    return make_response(jsonify({
        "status":200,
        "data": all
    }),200)

@offices_bp_v2.route('/offices/<int:my_office_id>',methods = ['GET'])
def get_office_by_id(my_office_id):
    my_office = office.get_by_id(my_office_id)
    if my_office:
        return make_response(jsonify({
            "status":200,
            "office": my_office
        }),200)
    return make_response(jsonify({
        "status":404,
        "error": "Office not found."
    }),404)