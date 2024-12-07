import sqlite3
import json

import db_json as dj

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
    
def get_users():
    conn, c = open_connection()
    c.execute('SELECT * FROM Users')
    users = c.fetchall()
    close_connection(conn)
    return dj.get_dict_users(users)

def get_user(username):
    conn, c = open_connection()
    c.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = c.fetchone()
    close_connection(conn)
    return dj.get_dict_user(user)
    
# add a new user whose data was passed in the request
def add_user(request):
    user_data = request.json
    conn, c = open_connection()
    c.execute('''
    INSERT INTO Users (username, password, email)
    VALUES (?, ?, ?)
    ''', (user_data['username'], user_data['password'], user_data['email']))
    conn.commit()
    close_connection(conn)
    # return if add operation was successful
    return json.dumps({'success': True})
     
  
def open_connection():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    return conn, c

def close_connection(conn):
    conn.close()
    
def clear_database():
    conn, c = open_connection()
    c.execute('DELETE FROM Users')
    conn.commit()
    close_connection(conn)