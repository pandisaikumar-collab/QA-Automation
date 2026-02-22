"""
> A module demonstrating duck typing in Python.
> duck typing is a concept related to dynamic typing
> where the type or class of an object is less important
> if an object has the required methods or attributes,
> python will use it __ without checking its actual type (class or type)
"""
class A:
    def m1(self):
        return 'Method m1 from class A'

class B:
    def m1(self):
        return 'Method m1 from class B'

class C:
    def m1(self):
        return 'Method m1 from class C'

def use_m1(obj):
    return obj.m1()

print(use_m1(A()))
print(use_m1(B()))
print(use_m1(C()))
# > python never checks the type of the object passed to use_m1
# > it only checks if the object has the method m1

# Example2:
class Car:
    def move(self):
        return 'Car is moving'

class Person:
    def move(self):
        return 'Person is walking'

def make_move(object):
    return object.move()

print(make_move(Car()))
print(make_move(Person()))























