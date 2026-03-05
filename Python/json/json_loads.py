import json

json_data = '{"a": 10, "b": 20, "c": 30}'
conv_dict = json.loads(json_data)
print(conv_dict)
print(type(conv_dict))