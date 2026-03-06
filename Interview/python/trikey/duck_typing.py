# Duck Typing:
# Duck typing is which is don't care about the type of the object,
# but care about the behavior of the object.
# Example:


class Add:
    def calculate(self, a, b):
        return a+b

class Sub:
    def calculate(self, a, b):
        return a-b

def perform_operation(operation, a, b):
    return operation.calculate(a, b)

print(perform_operation(Add(), 5, 3))  # Output: 8
print(perform_operation(Sub(), 5, 3))  # Output: 2


# how it works:
# in the above example, we have two classes Add and Sub,
# both classes have a method called calculate, which takes two parameters
# and returns the result of the operation.
# we have a function called perform_operation,
# which takes an operation and two parameters,
# and calls the calculate method of the operation.
