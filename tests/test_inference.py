import requests

url = "http://127.0.0.1:8000/infer"
data = {"inputs": [[1.0], [2.0], [3.0]]}
response = requests.post(url, json=data)
print(response.json())

url = "http://127.0.0.1:8000/health"
response = requests.get(url)
print(response.json())
