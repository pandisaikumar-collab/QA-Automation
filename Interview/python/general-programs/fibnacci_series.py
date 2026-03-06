"""
Fibonacci series:
 - A fibonacci series is sequence where each number is the sum of the
   previous two numbers.

   0 1 1 2 3 5 8 13 21 ...

"""

n=20

a=0
b=1

for i in range(n):
    print(a)
    c = a + b # calculate next number
    a = b
    b = c



"""
calculate next number: 
    0 + 1 = 1
    1 + 1 = 2
    1 + 2 = 3
    2 + 3 = 5

update values:
    a = b
    b = c
    
"""