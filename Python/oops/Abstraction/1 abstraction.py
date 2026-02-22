"""
Abstraction -hiding process 
Day-67
"""

class sample:
    __x=100  #now x is hidden and can be accessed from only within the class 
    y=200 
    print(__x)
    print(y)
    def display(self):
        print(sample.__x, type(sample.__x))
        print(sample.y, type(sample.y))


#end of class 
s1=sample()
s1.display()
#print(sample.__x) #can't be accessed from outside the class 
print(sample.y)

class test:
    a=300 
    def show(self):
        print(test.a)
        print(sample.y)
        #print(sample.__x) can not access 

t1=test()
t1.show()