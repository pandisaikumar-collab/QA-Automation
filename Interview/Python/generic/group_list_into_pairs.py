a = ['1', '2', '3', '4']
#o/p = ['12', '34']

result = []
i = 0
while i < len(a):
    pair = a[i] + a[i+1]
    result.append(pair)
    i += 2
print(result)

res = []
for i in range(0, len(a), 2):
    res.append(a[i] + a[i+1])
print(res)

results = []
for x, y in zip(a[::2], a[1::2]):
    results.append(x + y)
print(results)























