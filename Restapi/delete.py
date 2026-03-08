import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(url)
print(response.status_code)
print(response.json())