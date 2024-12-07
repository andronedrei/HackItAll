from flask import Flask, render_template, request, redirect, url_for, jsonify
import database_operations as db
import sqlite3
import json

employees = [ { 'id': 1, 'name': 'Ashley' }, { 'id': 2, 'name': 'Kate' }, { 'id': 3, 'name': 'Joe' }]

app = Flask(__name__)

@app.route('/')
def index():
    conn, c = db.open_connection()
    c.execute('SELECT * FROM users')
    my_tasks = c.fetchall()
    db.close_connection(conn)
    return render_template('index.html', tasks=my_tasks)

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    conn, c = db.open_connection()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    db.close_connection(conn)
    return jsonify(users)

# Add a new user
@app.route('/users', methods=['POST'])
    


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