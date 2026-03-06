list1 = [1,2,3,4,5,5,6,7,7]

res_consecutive = []

for i in range(1, len(list1)):
    if list1[i] == list1[i-1]:
        res_consecutive += [list1[i-1]]
        res_consecutive += [list1[i]]

        # use res_consecutive.append(list1[i-1])
        # res_consecutive.append(list1[i])

print(res_consecutive)


# line5: we are comparing current element list1[i] and previous element list1[i-1]
  # if started from 0, i-1 would be -1 (last-element), which is wrong.

# list1[i] - current element
# list1[i-1] - previous element
# if both are equal - they are consecutive duplicates
# why appended both: we add: first 5, second 5










