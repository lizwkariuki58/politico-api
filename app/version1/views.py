from flask import Blueprint,jsonify,request,make_response

from app.version1.models import PoliticalParty

parties_bp= Blueprint('parties',__name__)

@parties_bp.route('/parties', methods = ['GET'])
def get_all_parties():
    party = PoliticalParty()
    return jsonify(party.get_parties())
