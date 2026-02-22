#defining multple methods within the class
#modifying the values of static variables using a method 

class test:
    x=10
    y=20
    def m1(self):
        print(test.x)
        print(test.y)
        test.x=30
        test.y=40
    
    def m2(self):
        print(test.x)
        print(test.y)


t1=test() #here object stored into reference variable t1. 
t1.m1()
t1.m2()

t2=test()
t2.m1()
t2.m2()