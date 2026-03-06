"""
Method overloading:
    1. same method name but different number of arguments or different types of arguments
    2. the method behaves differently based on the inputs

"""

class A:

    def add(self, a, b=False, c=False):
        if b:
            return a+b

        elif c:
            return a+c

        elif b and c:
            return a+b+c

        else:
            return a

a1 = A()
print(a1.add(1))
print(a1.add(2,2))
print(a1.add(3,3, 3))

