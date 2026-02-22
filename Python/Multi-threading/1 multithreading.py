"""
MULTITHREADING:
Day-72
"""

# The process of executing 2 or more threads (logics) simultaneously is known as MultiThreading. 

class x: 
    def m1(self):
        for p in range(20):
            print(p)

    def m2(self):
        for q in range(10,20):
            print(q)

x1=x()
x1.m1()
x1.m2()


#here 1st m1() method logic executes an then 
#m2() method logic is executed, here execution is sequential, if i want parllel then go 
#for multithreading
