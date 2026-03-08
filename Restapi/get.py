# GET: used to fetch the data
import requests
import json

response = requests.get("https://api.github.com/events")
data = response.json()

print("Response data: ", data)
print("Status code: ", response.status_code)
print("Response headers: ", response.headers)
print("Response Time: ", response.elapsed.total_seconds())

## json body validation
if isinstance(data, list):
    print('data is list type')
else:
    print('data is not list type', type(data))

## validate keys
assert 'id' in data[0]
assert 'type' in data[0]

## validate data types
assert isinstance(data[0]['id'], str)
assert isinstance(data[0]['type'], str)

## validate not empty
assert len(data) > 0

## schema validation
# pip install jsonschema

from jsonschema import validate

from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "type": {"type": "string"}
    },
    "required": ["id", "type"]
}
print(schema)
validate(instance=data[0], schema=schema)

## response content validation
assert response.text != ''
assert len(response.content) > 0

























