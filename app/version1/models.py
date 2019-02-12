
class PoliticalParty():
    """ This class creates the blueprint for creating political parties. """

    parties=[]
   
    def __init__(self, id, name, hqAddress, slogan):
        self.id= id
        self.name= name
        self.hqAddress = hqAddress
        self.slogan= slogan
        
    def create_party(self):
        party = {
                'id': len(self.parties)+1,
                'name': self.name,
                'hqAddress': self.hqAddress,
                'slogan':self.slogan
            }
        self.parties.append(party)

    def get_parties(self):
        return self.parties
