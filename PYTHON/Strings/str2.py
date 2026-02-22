#string slicing: extracting particular portion of a string 

x='python program'

print(x[0:6]) #aways upper bound is executed 

print(x[7:11])

print(x[11:7]) #empty string ------> because always slicing is forward direction

print(x[-7:-3]) #using -ve index 

print(x[7:14])
print(x[7: ])

print(x[-7:11])
print(x[0:15:2]) #(start value, stop value, step value)
print(x[::2])
print(x[::-1]) #it reverses
