even_nums = []

for i in range(100):
    if i % 2 == 0:
        even_nums.append(i)
    else:
        continue
print(sum(even_nums))
