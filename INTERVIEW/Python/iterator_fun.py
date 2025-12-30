"""
Iterator functions:
 > Gives one value at a time from a collection
 > Remembers where it stopped last time
 > It does not give all values at once
 > Use less memory
 uses __iter__()
 uses __next__()
"""
numbers = [1, 2, 3, 4, 5]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))

for num in it:
    print(num)

# custom iterator
class Count:
    def __init__(self, max):
        self.num = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.max:
            self.num += 1
            return self.num
        else:
            raise StopIteration
counter = Count(5)
for count in counter:
    print(count)






