# convert to list key and value format:

data = ['A', 10, 'B', 20, 'C', 30, 'D', 40]


for k,v in zip(data[::2], data[1::2]):
    print(f'{k}={v}')

print('\n')

for i in range(0, len(data), 2):
    print(f'{data[i]}={data[i+1]}')