import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos')
print(response.json())
print(response.status_code)
print(response.text)
print(response.headers['Content-Type'])
print(response.elapsed.total_seconds())
