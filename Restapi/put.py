"""
PUT: completely replace existing values
"""

import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(url)
print(response.json())

payload = {'userId': 1, 'id': 10, 'title': 'put method...e', 'completed': True}
response = requests.put(url, data=json.dumps(payload))
print(response.json())
print(response.text)
print(response.headers)
print(response.status_code)
print(response.elapsed.total_seconds())
