from app.database_config import init_db
from app.version2.models.base_model import BaseModel
from BaseModel import check_if_exists

class UserModel(BaseModel):
    def __init__(self, firstname, lastname, email, phoneNumber, passportUrl, isAdmin):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phoneNumber= phoneNumber
        self.passportUrl = passportUrl
        self.isAdmin = isAdmin

    def save_user(self):
        user= {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "passportUrl": self.passportUrl,
            "isAdmin":self.isAdmin
        }

        conn = init_db()
        cur = conn.cursor()
\
        if check_if_exists('users', 'email', user[email]):
            return "User already exists"
        
        query = (""" INSERT INTO users (firstname, lastname, email, phoneNumber, passportUrl, isAdmin) VALUES \ (%(firstname)s, %(lastname)s, %(email)s, %(phoneNumber)s, %(passportUrl)s, %(isAdmin)s) RETURNING id """)
        cur.execute(query, user)
        id = cur.fetchone()[0]

        conn.commit()
        conn.close()

        return id

        def get_user(self):
            pass