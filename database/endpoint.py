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

if __name__ == '__main__':
    db.create_database()
    app.run(debug=True, host='0.0.0.0', port=5000)