dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

new_dict = dict1.copy()
new_dict.update(dict2)
print(new_dict)

new_dict = {**dict1, **dict2}
print(new_dict)