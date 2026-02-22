"""
1) Garbage colector is a pre-defined program or application or background
thread which is invoked by the python interpreter whenever any object 
reference count become zero at the time of execution of the program.

2) Garbage collector removes the unused or unreferenced objects from the memory location.

3) if any object reference count becomes as as zero, then we call that object as a unused or unrefernced object. 

4) refernce count is eqal to the number of reference variables pointing to that object 

"""

class test:
    pass 

t1=test()
t2=t1 
t3=t1 

#here all 3 reference are storing address(pointing) of 
#same object, so R.C=3 which is equal to no of ref variables (3)

del t3 #RC decreases by 1 RC=2 object is not removed 
del t2 #RC decreases by RC=1 object is not removed 
del t1 #RC decreases by to 0 object is removed by Garbage Collector. 

