a = "python online compiler"

b = " "
words = a.split(b)
result = []
for word in words:
    result.append(word[0])
print(result)

results = [word[0] for word in a.split(' ')]
print(results)

result = list(map(lambda word: word[0], a.split(b)))
print(result)

