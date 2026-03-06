"""
Method Overriding:
    1. same method names and same number of arguments
"""

class A:
    def add(self, a, b):
        return a + b

class B(A):
    def add(self, a, b, c):
        return a + b + c

b1 = B()
print(b1.add(1, 2, 3))