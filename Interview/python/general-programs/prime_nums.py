"""
Prime Numbers: prime number is a positive integer, it should be grater tan 1
exm: 2, 3, 7, 11, 13
"""

n=20

for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

