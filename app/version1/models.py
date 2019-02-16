parties=[]
offices = []

class PoliticalParty:
    """ This class creates the blueprint for creating political parties. """
   
    def __init__(self,name=None, hqAddress=None, slogan=None):
        self.id= len(parties)+1
        self.name= name
        self.hqAddress = hqAddress
        self.slogan= slogan
        
    def create_party(self):
        party= {
            'id':len(parties)+1,
            'name':self.name,
            'hqAddress': self.hqAddress,
            'slogan': self.slogan
        }

        parties.append(party)
        return parties
    
    def get_parties(self):
        return parties

class GovernmentOffice:
    """This class creates a blueprint for creating government offices"""
    def __init__(self,office_type=None, name=None):
        self.id= len(offices)+1
        self.type=office_type
        self.name=name



    
