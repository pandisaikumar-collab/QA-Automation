list1 = ['hello', 'take']
list2 = ['care', 'sir']

#output: ['hellocare', 'hellosir', 'takecare', 'takesir']

combinations = []
for item1 in list1:
    for item2 in list2:
        combinations.append(item1 + item2)
print(combinations)

results = [i + ' ' + j for i in list1 for j in list2]
print(results)

