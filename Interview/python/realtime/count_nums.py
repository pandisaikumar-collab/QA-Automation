nums = [1, 1, 2, 2, 3, 4, 5]

count_dict = {}
for num in nums:
    if num in count_dict:
        count_dict[num] +=1
    else:
        count_dict[num] = 1

print(count_dict)


from collections import Counter

count_dict = Counter(nums)
print(count_dict)