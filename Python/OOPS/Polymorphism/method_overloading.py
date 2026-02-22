"""
> same method name
> different number of arguments
> different types of arguments
* method overloading is not directly supported in Python
    like in some other languages (e.g., Java, C++)
> if we write the same method name many times in a class,
 the latest definition will override the previous ones.
This will not work: (only the seconds one will work)
class Test:
    def add(self, a, b):
        return a + b
    def add(self, a, b):
        return a + b

Achieve method overloading:
 > using default arguments
 > using *args (any number of inputs)
 > using **kwargs (any number of keyword inputs)
"""
class Test:
    def add(self, a, b, c=0):
        return a + b + c

t1 = Test()
print(t1.add(1, 2))
print(t1.add(2,2,2))

class Test2:
    def add(self, *args):
        return sum(args)

t2 = Test2()
print(t2.add(1,2,3,4,5))

class Test3:
    def show(self, data):
        if isinstance(data, int):
            print("Number: ", data)
        elif isinstance(data, float):
            print("Float: ", data)
        else:
            print("Other type: ", data)

t3=Test3()
t3.show(data=10)