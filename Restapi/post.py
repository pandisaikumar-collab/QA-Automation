# PUT: used to create new resource

import requests
import json

payload = {
    "userId": 1,
    "title": "Buy milk",
    "completed": False
}

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.post(url, json=payload)
print(response.json())
print(response.status_code)
print(response.text)
print(response.headers)
print(response.elapsed.total_seconds())


#manual serialization if not using json keyword, supply the json data

payload = {
    "userId": 1,
    "title": "Buy milk",
    "completed": True
}

headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.json())
print(response.status_code)
print(response.text)
print(response.headers)
print(response.elapsed.total_seconds())























