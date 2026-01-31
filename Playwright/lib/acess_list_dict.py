table_data = [{'firstname': 'Cierra', 'lastname': 'Vega', 'age': '39', 'email': 'cierra@example.com', 'salary': '10000', 'department': 'Insurance'}, {'firstname': 'Alden', 'lastname': 'Cantrell', 'age': '45', 'email': 'alden@example.com', 'salary': '12000', 'department': 'Compliance'}, {'firstname': 'Kierra', 'lastname': 'Gentry', 'age': '29', 'email': 'kierra@example.com', 'salary': '2000', 'department': 'Legal'}, {'firstname': '', 'lastname': '', 'age': '', 'email': '', 'salary': '', 'department': ''}, {'firstname': '', 'lastname': '', 'age': '', 'email': '', 'salary': '', 'department': ''}, {'firstname': '', 'lastname': '', 'age': '', 'email': '', 'salary': '', 'department': ''}, {'firstname': '', 'lastname': '', 'age': '', 'email': '', 'salary': '', 'department': ''}, {'firstname': '', 'lastname': '', 'age': '', 'email': '', 'salary': '', 'department': ''}, {'firstname': '', 'lastname': '', 'age': '', 'email': '', 'salary': '', 'department': ''}, {'firstname': '', 'lastname': '', 'age': '', 'email': '', 'salary': '', 'department': ''}]

emails = []
for data in table_data:
    emails.append(data['email'])
print(emails)

print(table_data[2])
