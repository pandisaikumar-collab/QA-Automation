"""
Generator:
> Returns values one by one
> uses less memory
> yield keyword pauses the function
> sends one value
> remember where it stopped
> continues from there next time
> saves memory/ Good for large data/ Faster startup
"""

def generator_fun(nums):
    for i in nums:
        yield i
        yield i
        yield i

gen = generator_fun([1,2,3,4,5])
print(next(gen))
print(next(gen))
print(next(gen))