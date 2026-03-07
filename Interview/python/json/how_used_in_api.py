import requests
import json

payload = {
    'userName': 'admin',
    'password': 'password_123'
}


response = requests.post('url', data=json.dumps(payload))
results = response.json() # deserialization


