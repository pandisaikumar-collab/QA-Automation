"""
> json.dump(), json.dumps(), json.load(), json.loads() in Python

> json.dump(): writes a python object to a file in JSON format.
> json.dumps(): converts a python object to a JSON string.

> json.load(): reads a JSON object from a file and converts it to a
  python object.
> json.loads(): converts a JSON string to a python object.
"""
import json

# dump() example: converts python dictionary to JSON, writes it into a file
data = {'name': 'a', 'age': 30, 'city': 'New York'}
with open('data.json_dump', 'w') as file:
    json.dump(data, file)

# dumps(): example: converts python dictionary to JSON string
data = {'name': 'b', 'age': 25, 'city': 'Los Angeles'}
json_str = json.dumps(data)
print(json_str)

# load() example: reads JSON object from a file, converts it to python object:
with open('data.json_dump', 'r') as file:
    data = json.load(file)
print(data)

# loads() example: converts JSON string to python object
json_str = {"name": "c", "age": 28, "city": "Chicago"}
data = json.dumps(json_str)
print(data)


























