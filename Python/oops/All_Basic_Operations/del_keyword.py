class test:
    pass 

t1=test() #RC=1
print(t1) 
del t1 #RC becomes 0, garbage collector is called and object removed. 

print(t1)


"""
del keyword is not for removing object, it is used to decrese the refernce 
count by 1, when RC=0, garbage collector is called and destructor executed.
"""

class test:
    def __init__(self):
        print("constructor called.")
    def __del__(self):
        print("destructor called")

