dict_1 = {
    'Cierra': {'Firstname': 'Cierra', 'Lastname': 'Vega', 'Age': '39', 'Email': 'cierra@example.com', 'Salary': '10000','Department': 'Insurance'},
    'Alden': {'Firstname': 'Alden', 'Lastname': 'Cantrell', 'Age': '45', 'Email': 'alden@example.com', 'Salary': '12000', 'Department': 'Compliance'},
    'Kierra': {'Firstname': 'Kierra', 'Lastname': 'Gentry', 'Age': '29', 'Email': 'kierra@example.com', 'Salary': '2000', 'Department': 'Legal'},
    '': {'Firstname': '', 'Lastname': '', 'Age': '', 'Email': '', 'Salary': '', 'Department': ''}
}

# 1. accessing elements
for key in dict_1:
    print(dict_1[key])

# 2. accessing specific element
for key in dict_1:
    print(dict_1[key]['Email'])

# 3. accessing keys
for key in dict_1.keys():
    print(key)

# 4. accessing values
for value in dict_1.values():
    print("Lastname: ", value['Lastname'])

# 5. accessing items
for item in dict_1.items():
    print(item)

# 6. accessing nested dictionary keys
for key in dict_1:
    for nested_key in dict_1[key]:
        print(nested_key)

# 7. accessing nested dictionary values
for key in dict_1.keys():
    for nested_key in dict_1[key].values():
        print(nested_key)

# 8. accessing nested dictionary items
for key in dict_1:
    for nested_key in dict_1[key].items():
        print(nested_key)


















