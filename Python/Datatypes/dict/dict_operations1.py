# create empty dictionary
d = {}

# create dictionary with values
d = {'a': 1, 'b': 2, 'c': 3}
print(len(d))
print(d)

#create dictionary using dict() function
d = dict(a=1, b=2)
print(d['a'])
print(d.get('b'))
print(d.get('d', 'Engineer'))
print(d.get('d')) # returns None

# add new key-value
d['d'] = 4
print(d)
d['name'] = 'sai'
print(d)

# update existing
d['name'] = 'sai kumar'
print(d)

# update multiple key-values
d.update({'city': 'hyd', 'country': 'india'})
print(d)

# remove key-value
d.pop('country')
print(d)

# remove last inserted item
d.popitem()
print(d)

# delete key
del d['d']
print(d)

# clear dictionary
d.clear()
print(d)

# copy dictionary
dict1 = {'x': 10, 'y': 20, 'z': 30}
dict2 = dict1.copy()
print(dict1)
print(dict2)

if 'x' in dict1:
    print("x is present in dict1")
else:
    raise ValueError("x is not present in dict1")

# get all keys
print(dict1.keys())
print(type(dict1))

# get all values
print(dict1.values())

# get all key-value pairs
print(dict1.items())

# iterate through keys
for k in dict1.keys():
    print(k)

# iterate through values
for v in dict1.values():
    print(v)

# iterate through dictionary
for k,v in dict1.items():
    print(k,v)

# nested dictionary
nested_dict = {
    'user1': {'name': 'sai', 'age': 26},
    'user2': {'name': 'kumar', 'age': 28},
    'user3': {'name': 'ravi', 'age': 24}
}

print(nested_dict)

for key,value in nested_dict.items():
    user2 = nested_dict['user1']['name']
print(user2)

list_of_dicts = [
    {'id': 1, 'name': 'a'},
    {'id': 2, 'name': 'b'},
    {'id': 3, 'name': 'c'}
]

for all_items in list_of_dicts:
    print(all_items)

# list inside dictionary
dict_with_list = {'skills': ['python', 'java']}
print(dict_with_list['skills'][0])

dict3 = dict2 | dict_with_list
print(dict3)

# deep copy = fully independent copy
import copy
copy_dict = copy.deepcopy(dict_with_list)
print(copy_dict)

from collections import defaultdict
dd = defaultdict(int)
print(dd)

from collections import Counter
e1 = "cabbed"
result = {}

for ch in e1:
    if ch in result:
        result[ch] = result[ch] + 1
    else:
        result[ch] = 1
print(result)

employee = {
    'id': 101,
    'personal_info': {
        'name': 'sai',
        'age': 26
    },
    'skills': {
        'primary': 'python',
        'secondary': 'selenium'
    }
}
# print(employee['skills'])
# print(employee['personal_info'])
# print(employee['id'])

for key in employee:
    print(key)
    if key == 'personal_info':
        for inner_key in employee[key]:
            print(inner_key, employee[key][inner_key])


users = [
    {"id": 1, "name": "A", "role": "admin"},
    {"id": 2, "name": "B", "role": "user"},
    {"id": 3, "name": "C", "role": "user"}
]

roles = []
ids = []
for user in users:
    roles.append(user['role'])
    ids.append(user['id'])
    # ids.remove(user['id'] - 1)
    # print(ids)

print(roles)

for user in users:
    if user['id'] == 2:
        user['id'] = 15
print(users)

for user in users:
    user['city'] = 'bgl'
print(user)

print('\n')
employees = [
    {
        "id": 1,
        "info": {"name": "A", "dept": "IT"}
    },
    {
        "id": 2,
        "info": {"name": "B", "dept": "HR"}
    }
]

for emp in employees:
    print(emp['info']['name'])
    emp['info']['location'] = 'hyd'
    emp['info']['location'] = 'bgl'
    emp.update({'status': 'active'})












































































































