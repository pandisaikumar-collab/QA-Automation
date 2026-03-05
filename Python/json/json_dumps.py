import json

dict_data = {'name1': 1, 'name2': 2, 'name3': 3}
conv_json = json.dumps(dict_data)
print(conv_json)
print(type(conv_json))