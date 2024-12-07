import sqlite3
import json

database = 'database.db'

def create_database():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # Creeate a table with autoincement id, username, password and email
    c.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()
    
# add a new user whose data was passed in the request
def add_user(request):
    user_data = request.json
    
    
def open_connection():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    return conn, c

def close_connection(conn):
    conn.close()