d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 3, 'c': 4, 'd': 5}

result = {}
for k in d1:
    found=False
    for j in d2:
        if k == j:
            found=True
    if found==False:
        result[k] = d1[k]

for k in d2:
    found=False
    for j in d1:
        if k == j:
            found=True
    if found==False:
        result[k] = d2[k]

print(result)
