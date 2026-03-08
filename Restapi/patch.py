"""
PATCH: modify the value of a specific field on existing data
"""
import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/10"
payload = {
    'title': 'Patch request'
}

response = requests.patch(url, json=payload)
print(response.text)
print(response.status_code)
print(response.headers)
print(response.json())
print(response.elapsed.total_seconds())

