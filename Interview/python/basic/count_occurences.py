input_list = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

count_dict = {}

for item in input_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)


# if already seen - increase count
# if first time - set count 1

from collections import Counter

count_dict = Counter(input_list)
print(count_dict)