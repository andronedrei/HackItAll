from flask import Flask, render_template, request, redirect, url_for, jsonify
import database_operations as db
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def index():
    conn, c = db.open_connection()
    c.execute('SELECT * FROM users')
    my_tasks = c.fetchall()
    db.close_connection(conn)
    return render_template('index.html', tasks=my_tasks)

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(db.get_users())

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    return jsonify(db.add_user(request))

@app.route('/users/<username>', methods=['PUT'])
def update_user_route(username):
    return jsonify(db.update_user(username, request))

# get a single user
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    return jsonify(db.get_user(username))


# @app.route('/add', methods=['POST'])
# def add_task():
#     task = request.form['task']
#     conn = sqlite3.connect('todo.db')
#     c = conn.cursor()
#     c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('index'))

# @app.route('/delete/<int:task_id>')
# def delete_task(task_id):
#     conn = sqlite3.connect('todo.db')
#     c = conn.cursor()
#     c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('index'))

def reset_users_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Drop the old table if it exists
    c.execute('DROP TABLE IF EXISTS Users;')
    print("Old 'Users' table dropped.")

    # Recreate the table with the new schema
    c.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        phone TEXT,
        date_of_birth TEXT,
        nationality_country TEXT,
        nationality_city TEXT,
        residence_country TEXT,
        residence_city TEXT,
        profile_picture TEXT,
        latitude REAL,
        longitude REAL
    );
    ''')
    conn.commit()
    conn.close()
    print("New 'Users' table created successfully.")


if __name__ == '__main__':
    #reset_users_table()
    db.create_database()
    app.run(debug=True, host='0.0.0.0', port=5000)