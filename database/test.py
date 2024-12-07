import requests
import database_operations as db

def send_request(method, extra_url, json=None, params=None):
    response = requests.request(method, base_url + extra_url, json=json, params=params)
    print(response.status_code)
    print(response.json())
    return response

# The base URL of your Flask app
base_url = "http://127.0.0.1:5000"

# Send the POST request with the JSON data
response = send_request('POST', '/users', json={
    'username': 'testuser',
    'password': 'testpassword',
    'email': 'avsah@nxsjn'
})

print("_________________")

response = send_request('POST', '/users', json={
    'username': 'testuser2',
    'password': 'testpassword2',
    'email': 'avsah@nxsjn'
})

print("_________________")

response = send_request('GET', '/users')

print("_________________")

response = send_request('GET', '/users/testuser')

# importa vaza de date si dai clear
# db.clear_database()
    
