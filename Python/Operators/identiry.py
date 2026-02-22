"""
Identity operators: These operators are used to compare the address 
                    of objects

identity operators alos returns True/False 

1) is
2) is not 

"""
a=10
b=20

print(a,id(a))
print(b,id(b))

print(a is b) #compares the address 
print(a==b) #compares the content 
print(a is not b ) 