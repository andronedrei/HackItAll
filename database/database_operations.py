import sqlite3
import json

import db_json as dj

database = 'database.db'

def create_database():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # Creeate a table with autoincement id, username, password and email
    # c.execute('''DROP TABLE IF EXISTS Users;''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        first_name TEXT DEFAULT '',
        last_name TEXT DEFAULT '',
        age INTEGER DEFAULT 0,
        phone TEXT DEFAULT '',
        date_of_birth TEXT DEFAULT '',
        nationality_country TEXT DEFAULT '',
        nationality_city TEXT DEFAULT '',
        residence_country TEXT DEFAULT '',
        residence_city TEXT DEFAULT '',
        profile_picture TEXT DEFAULT '',
        latitude REAL DEFAULT 0.0,
        longitude REAL DEFAULT 0.0
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


# Function to get a single user by username
def get_user(username):
    conn, c = open_connection()

    # Query the database to find the user by username
    c.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = c.fetchone()  # This will return the first matching row, or None if no match is found

    close_connection(conn)

    # If a user is found, return the user data in a dictionary form
    if user:
        # Constructing the dictionary based on your table columns
        user_dict = {
            'username': user[1],
            'password': user[2],
            'email': user[3],
            'first_name': user[4],
            'last_name': user[5],
            'age': user[6],
            'phone': user[7],
            'date_of_birth': user[8],
            'nationality_country': user[9],
            'nationality_city': user[10],
            'residence_country': user[11],
            'residence_city': user[12],
            'profile_picture': user[13],
            'latitude': user[14],
            'longitude': user[15]
        }
        return user_dict
    else:
        return None  # No user found


# add a new user whose data was passed in the request
def add_user(request):
    user_data = request.json
    conn, c = open_connection()
    try:
        c.execute('''
        INSERT INTO Users (username, password, email, first_name, last_name, age, phone, date_of_birth, nationality_country, nationality_city, residence_country, residence_city, profile_picture, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_data['username'], user_data['password'], user_data['email'], user_data.get('first_name', ''), user_data.get('last_name', ''), user_data.get('age', 0), user_data.get('phone', ''), user_data.get('date_of_birth', ''), user_data.get('nationality_country', ''), user_data.get('nationality_city', ''), user_data.get('residence_country', ''), user_data.get('residence_city', ''), user_data.get('profile_picture', ''), user_data.get('latitude', 0.0), user_data.get('longitude', 0.0)))
        conn.commit()
    except sqlite3.IntegrityError as e:
        return json.dumps({'success': False, 'message': 'Username already exists'}), 400
    finally:
        close_connection(conn)
    # return if add operation was successful
    return json.dumps({'success': True})


def update_user(username, request):
    # Retrieve the new data from the incoming request body
    user_data = request.json

    # Open the database connection
    conn, c = open_connection()

    # Check if the user exists
    c.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = c.fetchone()

    if not user:
        close_connection(conn)
        return json.dumps({'success': False, 'message': 'User not found'}), 404

    # Update the user's data in the database using the new values from user_data
    c.execute('''
    UPDATE Users
    SET
        password = ?,
        email = ?,
        first_name = ?,
        last_name = ?,
        age = ?,
        phone = ?,
        date_of_birth = ?,
        nationality_country = ?,
        nationality_city = ?,
        residence_country = ?,
        residence_city = ?,
        profile_picture = ?,
        latitude = ?,
        longitude = ?
    WHERE username = ?
    ''', (
        user_data.get('password', user[1]),  # Retain the old value if not updated
        user_data.get('email', user[2]),
        user_data.get('first_name', user[3]),
        user_data.get('last_name', user[4]),
        user_data.get('age', user[5]),
        user_data.get('phone', user[6]),
        user_data.get('date_of_birth', user[7]),
        user_data.get('nationality_country', user[8]),
        user_data.get('nationality_city', user[9]),
        user_data.get('residence_country', user[10]),
        user_data.get('residence_city', user[11]),
        user_data.get('profile_picture', user[12]),
        user_data.get('latitude', user[13]),
        user_data.get('longitude', user[14]),
        username  # Ensure the correct user is updated
    ))

    # Commit the changes to the database
    conn.commit()
    close_connection(conn)

    # Return a success response
    return json.dumps({'success': True, 'message': 'User updated successfully'})

  
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