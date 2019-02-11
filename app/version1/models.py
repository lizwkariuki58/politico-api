class User:
    pass
class Party:
    parties = []
    id = 0
    name = ''
    hqAddress = ''
    slogan= ''

    def __init__(self):
        self.parties =[
            {
                'id': 1,
                'name': 'Gryffindor',
                'hqAddress': '4 Privet Drive',
                'slogan':'Where dwell the brave at heart!'
            },
            {
                'id': 2,
                'name': 'Slytherin',
                'hqAddress': '13 Spinners End'
                'slogan':'Without cunning, there can be no innovation'
            },

        ]

class GovernmentOffice:
    pass