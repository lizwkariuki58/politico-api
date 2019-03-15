import os
import psycopg2

main_uri= os.getenv('DB_URI')
test_uri= os.getenv('TEST_DB_URI')

def connection(uri):
    conn = psycopg2.connect(uri)
    return conn

def init_db():
    conn = connection(main_uri)
    cur = conn.cursor()
    queries = create_tables()

    for query in queries:
        cur.execute(query)
    conn.commit()
    return conn

def init_test_db(test_uri):
    conn = connection(test_uri)
    cur = conn.cursor()
    queries = create_tables()

    for query in queries:
        cur.execute(query)
    conn.commit()
    return conn

def destroy_db():
    conn = connection(test_uri)
    cur = conn.cursor()

    offices = """ DROP TABLE IF EXISTS offices; """
    users = """ DROP TABLE IF EXISTS users;
     """
    parties = """ DROP TABLE IF EXISTS parties; """

    queries = [offices, users,parties]
    
    for query in queries:
        cur.execute(query)
    conn.commit()
    return conn

def create_tables():
    offices = """ CREATE TABLE IF NOT EXISTS offices(
        office_id serial PRIMARY KEY NOT NULL,
        name VARCHAR(30) NOT NULL,
        office_type VARCHAR(30) NOT NULL
    );"""
    parties = """ CREATE TABLE IF NOT EXISTS parties(
        party_id serial PRIMARY KEY NOT NULL,
        name VARCHAR(30) NOT NULL,
        hqAddress VARCHAR(100) NOT NULL,
        logoUrl VARCHAR(50) NOT NULL
    );"""
    users = """ CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        firstname VARCHAR(30) NOT NULL, 
        lastname VARCHAR(30) NOT NULL,
        othername VARCHAR(30),
        email VARCHAR(30) NOT NULL,
        phoneNumber VARCHAR(30) NOT NULL,
        passportUrl VARCHAR(30) NOT NULL,
        isAdmin BOOLEAN DEFAULT False
    );"""

    queries = [offices, users, parties]
    return queries