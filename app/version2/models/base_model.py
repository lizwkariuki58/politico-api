from app.database_config import init_db

class BaseModel:
    def check_if_exists(self, table, field, value):
        conn = init_db()
        cur = conn.cursor()

        query = """SELECT * FROM {} WHERE {}='{}' """.format(table,field,value)

        cur.execute(query)
        response = cur.fetchall()
        if response:
            return True
        return False

    def get_value(self, table, field, pk, value):
        conn = init_db()
        cur = conn.cursor()

        query = """ SELECT {} FROM {} WHERE {} = '{}'""".format(field, table,pk,value)

        cur.execute(query)
        response = cur.fetchall()
        name = response[0][0]
        return name

