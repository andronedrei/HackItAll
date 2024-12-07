import requests

# The base URL of your Flask app
base_url = "http://127.0.0.1:5000/users"

# Define the username as a query parameter
params = {'username': 'testuser'}

# Send the GET request with the username parameter
response = requests.get(base_url, params=params)

# Print the response status code
print("Status Code:", response.status_code)

# Print the response data (JSON)
print("Response JSON:", response.json())
