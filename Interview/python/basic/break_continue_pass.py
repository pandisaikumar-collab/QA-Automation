
for i in range(10):
    if i == 2:
        break
    print(i)

print('\n')

even_num = []
for i in range(10):
    pass # nothing, for feature reference
    if i % 2 == 0:
        even_num.append(i)
print(even_num)

print('\n')

for i in range(10):
    if i == 5:
        continue
    print(i)




