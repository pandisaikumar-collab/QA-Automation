"""
> while loop runs again and again while a certain condition is true.
> Stop when condition becomes false.
while condition:
    statements
"""
# Basic examples
i = 1
while i <= 5:
    print(i)
    i += 1
print(i)

i = 5
while i > 0:
    print(i)
    i -= 1
print(i)

i = 0
while i < 10:
    print('Hello')
    i += 2
print(i)

p = 0
while p < 10:
    print('world')
    p += 1
print(p)

# While with if statements
i = 1
while i < 10:
    if i % 2 == 0:
        print('even: ', i)
    i += 1
print(i)

i = 1
while i < 10:
    if i % 2 != 0:
        print('odd: ', i)
    i += 1
print(i)

# While with break & continue
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
print(i)

i = 1
while i <= 10:
    i += 1
    if i  == 3:
        continue
    print(i)

i = 1
while True:
    if i > 5:
        break
    print(i)
    i += 1
print(i)

# While with list, string
nums = [10,20,30,40,50]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
print(i)

i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(i, j)
        j += 1
    i += 1
print(i)
























































