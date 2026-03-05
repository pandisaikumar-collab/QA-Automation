
def test_generator(nums):
    for num in nums:
        yield num


nums = [1, 2, 3, 4, 5]
t1=test_generator(nums)
print(next(t1))

print(list(t1))

# Generator return values one by one, not everything once
# Used for memory consumption when handling with large data



def normal_fun(nums):
    res_list = []
    for num in nums:
        res_list.append(num)
    return res_list

nums = [1, 2, 3, 4, 5]
n1 = normal_fun(nums)
print(n1)