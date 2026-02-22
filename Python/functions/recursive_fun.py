# A recursive function is a function that calls itself to solve a problem.
# it is commonly used in mathematical and divide-and-conquer problems.

def factorial(n):
    if n == 0:
        return 1
    else:
        return  n * factorial(n - 1)
print(factorial(4))
