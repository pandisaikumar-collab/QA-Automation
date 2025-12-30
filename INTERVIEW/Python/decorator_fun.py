# Decorator:
"""
> A decorator is a way to add additional functionality to an existing function
> without changing the function's code.

> we use decorator:
 1. add logging (print statements)
 2. add time tracking
 3. security checks
 4. add reusable functionality

All without touching the original function's code.
"""

# without decorator:

def say_hello(): # adding manually
    print('hello')
    print('welcome')

say_hello() # changed the original function  and hard to reuse

# with decorator:

def decorator_fun(func):
    def inner_fun():
        print('hello')
        func()
        print('welcome')
    return inner_fun

@decorator_fun
def say_hello():
    print('hello')
say_hello()


@decorator_fun
def say_goodbye():
    print('goodbye')
say_goodbye()


# Decorator with arguments:

def decorator_fun_args(func):
    def inner_fun_args(name):
        print('hello')
        func(name)
        print('welcome')
    return inner_fun_args

@decorator_fun_args
def greet(name):
    print('hello', name)
greet('Alice')

@decorator_fun_args
def farewell(name):
    print('goodbye', name)
farewell('Bob')


# *args and **kwargs in decorator:
# some function take 1 args, some take 2 or more args
# (*args> multiple values tuple, **kwargs> key value pari dictionary)

def decorator_fun_args(func):
    def inner_fun_args(*args, **kwargs):
        print('hello')
        func(*args, **kwargs)
        print('welcome')
    return inner_fun_args

@decorator_fun_args
def m1(name):
    print('m1 method')
m1('Alice')

@decorator_fun_args
def m2(name, age):
    print('m2 method')
m2('Bob', 30)

@decorator_fun_args
def m2(name='a', age=0):
    print('m2 method with kwargs')
m2(age=25, name='Charlie')


# real word example: timing decorator
import time
def time_tracker(func):
    def inner_fun(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time taken: ", end - start)
    return inner_fun

@time_tracker
def add(a, b):
    time.sleep(2)
    print("Addition: ", a + b)
add(5, 10)
















































