"""
What is self:
 > self means (the current object)
 > it is used inside a class methods to refer to the object that is using the class

Why do we need self:
 > when you create many objects from one class,
 > self helps python know which object you are talking about
 > Without self, python cannot store or read data correctly
"""
# with self:
class A:
    def __init__(self, name):
        self.name = name

a1 = A("Alice")
a2 = A("Bob")
 # each object keeps its own value

# without self:
class B:
    def __init__(name):
        name = name
#b1 = B("Charlie")
#b2 = B("David") # TypeError: B.__init__() takes 1 positional argument but 2 were given
# values are not stored in the objects

# Is self keyword:
# No, self is not a keyword in Python.
# it is just a strong convention,
# but you can use any name instead of self
# But not recommended






















