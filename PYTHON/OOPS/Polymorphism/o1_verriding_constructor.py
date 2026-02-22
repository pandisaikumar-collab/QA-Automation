"""
Overriding a constructor 
"""

class X: 
    def __init__(self):
        print("from constructor of X")

class Y(X):
    def __init__(self):
        print("from constrctor of y...")

y1=Y()

#here derived class constructor overrides base class constructor 

#if u want super class constructor to be executed, the create object of suepr class 

#x1=X()

help(X)