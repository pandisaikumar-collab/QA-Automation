numbers = [5, 2, 9, 1, 7]

n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j] #swap

print(numbers)

"""
1. compare the first two elements
2. if the first is grater than the second, swap them 
3. move to the next pair, repeat
4. repeat the whole process for remaining elements
"""