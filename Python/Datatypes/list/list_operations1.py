items = [10, 30, 20, 30, 30, 40, 50]

# 1.append - adds an item to the end of the list
items.append(60)
print(items)

# 2. insert - adds an item at a specified index
items.insert(0, 100)
print(items)

# 3. remove - removes the first occurrence of a specified item
items.remove(30)
print(items)

# 4. pop - removes and returns the item at the specified index
# (default is the last item)
popped_item = items.pop()
print(popped_item)
items.pop(2)
print(items)

# 5. clear - removes all items from the list
# items.clear()
# print(items)

# 6. index - returns the index of the first occurrence of a specified item
index_of_10 = items.index(10)
print(index_of_10)

# 7. count - returns the number of occurences of a specified item
count_of_30 = items.count(30)
print(count_of_30)

# 8. sort - sorts the items of the list in ascending order
items.sort() # it will sort the original list and return None
print(items)

# sorted in ascending order
sorted_list = sorted(items)
print(sorted_list)

# sorted in descending order
sorted_list_desc = sorted(items, reverse=True)
print(sorted_list_desc)

# using without build in methods all operations on list

list_2 = [10, 20, 30, 20, 40, 50, 30, 60]

# count elements without using count method
count = 0
for item in list_2:
    if item == 20:
        count += 1
print(count)

# sum elements
total = 0
for item in list_2:
    total = total + item
print(total)

# find index of an element
for i in range(len(list_2)):
    if list_2[i] == 10:
        print(i)
        break

# find maximum element
max_element = list_2[0]
for item in list_2:
    if item > max_element:
        max_element = item
print(max_element)

# find minimum element
min_element = list_2[0]
for item in list_2:
    if item < min_element:
        min_element = item
print(min_element)

# reverse a list
rev = []
i = len(list_2) - 1
print(i)
while i >= 0:
    rev = rev + [list_2[i]]
    i = i - 1
print(rev)

# sort a list in ascending order using bubble sort
# write comments to explain the logic
for i in range(len(list_2)):
    # iterate through each element in the list
    for j in range(0, len(list_2)-i-1):
        # itegrate through the list from 0 to len-i-1
        if list_2[j] > list_2[j+1]:
            # if the current element is grater than the next element,
            # swap the elements
            list_2[j], list_2[j+1] = list_2[j+1], list_2[j]
            # swapping using tuple unpacking
print(list_2)

# sort a list in descending order using bubble sort
for i in range(len(list_2)):
    for j in range(len(list_2)-i-1):
        if list_2[j] < list_2[j+1]:
            list_2[j], list_2[j+1] = list_2[j+1], list_2[j]
print(list_2)

# copy list
list_copy = []
for item in list_2:
    list_copy = sorted(list_copy + [item])
print(list_copy)

# merge two lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# merging 2 lists
merged_list = []
for item in list_a:
    merged_list = merged_list + [item]
print(merged_list)

for item in list_b:
    merged_list = merged_list + [item]
print(merged_list)

# check element is exist
found = False
for item in list_2:
    if item == 10:
        found=True
        break
print(found)

# count sepcefic element in the list
print(list_2)

count = 0
for item in list_2:
    if item == 30:
        count += 1
print(count)

# remove duplicate element from the list
unique_list = []
for item in list_2:
    if item not in unique_list:
        unique_list += [item]
        unique_list.sort()
print(unique_list)

lst = [1, 2, 3, 4]
evens = []
odd = []
for i in lst:
    if i % 2 == 0:
        evens = evens + [i]
    else:
        odd = odd + [i]
print(evens)
print(odd)

























