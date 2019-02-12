from flask import jsonify,request,make_response

class PoliticalParty():
    """ This class creates the blueprint for creating political parties. """

    parties=[]
   
    def __init__(self, id=0, name=None, hqAddress=None, slogan=None):
        self.id= 0
        self.name= name
        self.hqAddress = name
        self.slogan= name
        
    def create_party(self):
        req = request.get_json()
        new ={
        'id': len(self.parties)+1,
        'name': req['name'],
        'hqAddress':req['hqAddress'],
        'slogan':req['slogan']
        }

        self.parties.append(new)
        return make_response(jsonify({
            'message':'Party Created',
            'Party ID': new['id']
        }),)
    
    def get_parties(self):
        return make_response(jsonify({
            'Message': 'OK',
            'Parties': self.parties
        }),200)
