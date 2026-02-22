# swap two numbers without using a third variable

a, b = 5, 10
print('before swapping: ', a, b)

a = a + b # a now becomes 15
b = a - b # b becomes 5
a = a - b # a becomes 10
print('after swapping: ', a, b)

