import requests

res = requests.get("http://localhost:8000/auth/hello/")
print(res.json())
