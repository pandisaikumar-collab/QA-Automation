sentence = "python is good and python is easy and python is powerful"

count_dict = {}

for word in sentence.split():
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

#print(count_dict)

for key,value in count_dict.items():
    if value > 1:
        print(key,value)
