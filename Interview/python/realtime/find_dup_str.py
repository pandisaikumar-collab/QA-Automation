input_str = "python is a good program"

remove_spaces = input_str.replace(" ","")
print(remove_spaces)

res_dict = {}
for ch in remove_spaces:
    if ch in res_dict:
        res_dict[ch] += 1
    else:
        res_dict[ch] = 1

#print(res_dict)


for k,v in res_dict.items():
    if v > 1:
        print({k:v})