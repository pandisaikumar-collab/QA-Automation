# in python, variables are reference to objects,
# when we pass them to a function, the behavior
# depends on the mutability of the object (lists, dictionaries)
# or immutability of the object (integers, strings, tuples).

# Mutable objects: Changes inside the function affect the original object.
# Immutable objects: Changes inside the function do not affect the original object.

# Function modifies the first element of list
def fun1(x):
    x[0] = 20

x = [10, 30, 40]
fun1(x)
print(x)



















