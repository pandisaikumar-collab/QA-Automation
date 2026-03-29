# create list
list1 = [5,4,2,1,3]

# create list with range
list2 = list(range(1,10))
print(list2)

# access the element
print(list2[0])

# slice list
print(list2[0:5])

# append to list
list2.append(12)
print(list2)

# extend list
list3 = [13, 14, 15, 17, 16]
list2.extend(list3)
print(list2)

# insert
list2.insert(0, 100)
print(list2)

# remove by value
list2.remove(2)
print(list2)

# remove by index
list2.pop(2)
print(list2)

# count occurrences
print(list2.count(1))

# sort list
list2.sort()
print(list2)

# reverse=True
list2.sort(reverse=True)
print(list2)






































