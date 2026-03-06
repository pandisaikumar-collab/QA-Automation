"""
== vs is in Python
== checks value
is -> checks identity
"""

a = 10
b = 10
print(a == b) # True
print(a is b) # True

x = [1, 2, 3]
y = [1, 2, 3]

print( x == y) # True
print(x is y)  # False

# even through values are same
# they are different lists in memory
