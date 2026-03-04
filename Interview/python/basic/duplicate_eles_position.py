list1 = [10, 20, 30, 10, 40, 20, 50]

res_position = {}

for index,element in enumerate(list1):
    if element in res_position:
        res_position[element].append(index)
    else:
        res_position[element] = [index]

#print(res_position)

for key,value in res_position.items():
    if len(value) > 1:
        print(key,value)