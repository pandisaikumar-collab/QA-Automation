"""
> we use HTTP methods like GET, POST, PUT, DELETE
"""
# create POST  request
import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

