# an anonymous function means that a function is without a name.
# as already know the def keyword is used do define a normal function.

def cube(x):
    return x ** 3
print(cube(2))

cube1 = lambda x, y: x * y
print(cube1(2, 3))

addition = lambda x,y,z: x + y + z
print(addition(1, 2, 3))
