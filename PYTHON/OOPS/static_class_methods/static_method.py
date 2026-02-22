"""
@staticmethod
> A static method is like normal function,
> it does not use object data and does not use class data.
> It is bound to the class and not the object of the class.
> It can be called using the class name or using the object of the class.
> It cannot access or modify class state or instance state.

(No self, No cls, just a normal function kept inside a class)
> No object needed
> No class data used
> just logic

When to use static method?
 > method does not need object values
 > method does not need class values
 > just helper logic

"""
# Normal function inside class
# use self, works with object data
class Demo:
    def show(self):
        print("Normal function..")
d1 = Demo()
print(d1.show())

class TestUtils:
    @staticmethod
    def add(a, b):
        return a + b
print(TestUtils.add(3,3))


