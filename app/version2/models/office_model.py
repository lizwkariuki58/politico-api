import psycopg2
from app.database_config import init_db
from app.version2.models.base_model import BaseModel

class Office(BaseModel):
    def __init__(self,name='', office_type=''):
        self.name= name
        self.office_type = office_type
    
    def convert_to_json(self):
        office_json={
            "name":self.name,
            "office_type":self.office_type
        }
        return office_json

    def save(self):
        conn = init_db()
        cur = conn.cursor()

        bm= BaseModel()
        if bm.check_if_exists('offices', 'name', self.name)== True:
            return False

        args = self.name, self.office_type

        query = """INSERT INTO offices (name, office_type) VALUES (%s, %s) RETURNING office_id;"""
        cur.execute(query,(args[0],args[1]))

        conn.commit()
        cur.close()

    def get_all(self):
        conn = init_db()
        cur = conn.cursor()

        query = """SELECT * FROM offices; """

        cur.execute(query)
        rows = cur.fetchall()

        return rows

    def get_by_id(self,office_id):
        conn = init_db()
        cur = conn.cursor()

        if BaseModel().check_if_exists('offices', 'office_id',office_id):
            query = """ SELECT * FROM offices WHERE office_id =office_id;"""
            cur.execute(query)
            my_office = cur.fetchone()

            office = Office(my_office[1],my_office[2])

            return office.convert_to_json()
        return False
        
        