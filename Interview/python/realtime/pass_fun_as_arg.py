"""
Pass a function as an argument:

> in python, functions are like objects
> so, we can give a function to another function as an argument
"""

def function_a():
    print("Function A is called")

def function_b(func): # function as argument, can give any name to the parameter
    print('Function B is called')
    func()

function_b(function_a)

