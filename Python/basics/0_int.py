# Case 1: Defining a variable 

x=10
print(x)
print(id(x))
print(type(x))


# Case 2: defining 2 diff variables with 2 diff values then 2 diff object
#         gets created  wiht 2 diff address 

x=10
y=20

print(id(x))
print(id(y))

print(x)
print(y)

print(type(x))
print(type(y))

# Case 3: Defining diff varialbes with same values then only one object gets 
#         created and its address is returned to both the variables 

x=10
y=10

print(x)
print(id(x))
print(type(x))

print(y)
print(id(y))
print(type(y))
