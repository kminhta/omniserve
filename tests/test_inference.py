import requests

BASE_URL = "http://127.0.0.1:8000"

response = requests.get(f"{BASE_URL}/health")
print(response.json())

data = {"inputs": [[1.0], [2.0], [3.0]]}
response = requests.post(f"{BASE_URL}/infer", json=data)
print(response.json())
