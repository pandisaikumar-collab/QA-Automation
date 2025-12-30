"""
what is constructor:
> A constructor is a special method in python
> it runs automatically when you create an object from a class.

why do we need constructor:
> A class is a blueprint(plan)
> An object is the real thing made from that plan
> __init__ helps set initial values for that object

what is self:
> self means (this object)
> it helps the object remember its own values and methods

self.name = name (store name inside the object)

without constructor:
class A:
    pass

a = A()
a.name = "Alice"
a.age = 30
 > values are added manually after object creation
 > not safe if we forget to add them

 With constructor:
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = A("Alice", 30)
> values are set automatically when object is created
> Clean, safe, and organized

"""




















