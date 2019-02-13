class PoliticalParty():
    """ This class creates the blueprint for creating political parties. """

    parties=[]
   
    def __init__(self,name=None, hqAddress=None, slogan=None):
        self.id= len(self.parties)+1
        self.name= name
        self.hqAddress = hqAddress
        self.slogan= slogan
        
    def create_party(self):
        party= {
            'id':len(self.parties)+1,
            'name':self.name,
            'hqAddress': self.hqAddress,
            'slogan': self.slogan
        }

        self.parties.append(party)
        return self.parties
    
    def get_parties(self):
        return self.parties
