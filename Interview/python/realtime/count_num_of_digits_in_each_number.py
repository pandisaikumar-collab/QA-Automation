eles = [123, 1234, 12345, 1234567]

output = []

for ele in eles:
    output.append(len(str(ele)))
print(output)

#without using built-in function
output = []

for ele in eles: #iterating through each element in the list
    count = 0 #initializing count to 0 for each element
    while ele > 0: #loop will run until ele becomes 0
        ele = ele // 10 #dividing ele by 10 to remove the last digit
        count += 1 #incrementing count by 1 for each digit removed
    output.append(count)
print(output)