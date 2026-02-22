"""
Static Variables: The variables which are defined within the class and defined 
                  outside all the methods of a class are known as static variables.

ex: 
    class sample:
        x=10 #static variables, defined within the class and outside the method 
        def m1(self): #method 
            print(sample.x)
    print(sample.x)

properties of static variables:
-------------------------------
1) The data which is common for all the objects, then it is recommended
   represent by using static variables. 
    ex: bank name -----> SBI 
        withdralimit --> 25000

2) data which is changing object from one object to another object---> then
    use non-static variable
    ex: ename, eid, designation, salary 

3) for static variables, only once memeroy is allocated, as it is initalized only once. 

4) A static variable can be accessed by all the methods of that classes and also by other classes. 
    ex: 
        class sample: 
            x=10
            def display():
                print(sample.x)
            def show():
                print(sample.x)
    
    Here x is static variable which can be accessed by all the methods like display, show etc. 

5) A static variable always be accessed by using classname i.e from witin the class
   or outside the class also 
   ex:
      class sample:
        x=20
        y=10 
        def display(self):
            print(sample.x)
            print(sample.y)
        def show(self):
            print(sample.x)
            print(sample.y)
       
      print(sample.x)
      print(sample.y) #accessing SV from outside the class using classname 


diff b/w function and method:
=============================

Function:
---------
1. Funtion always defined outside the class 
2. Function called normally without object 
    ex: display()
3. For function, no need to self argument


Method:
-------
1. Method always defined within the class 
2. Method alwyas called uisng a object 
3. Method compusolily should have self argument. 


difference b/w Static variable and Non-static variable:
=======================================================
Static variable: 
----------------
1) for object ot object if data is common for for static variable 
   ex: company='TCS'
2) Always defined outside the class 
3) only once memory is allocated, as ititlized only once 
4) static variable is no way related to object 


Non-static variable:
--------------------
1) For object ot object if data is changing go for Non-static variable 
   ename=input("Enter the name: ")
2) always defined within the methods 
3) here multiple times memory is allocated, multiiple times they are initilized.
4) object is used to initalize a NSV without object NSV cannot be created or initilized. 

ex: eid=101
    eid-102 
    eid=203 

    if 3 objects --> 3 times NSV's are initlized 
    if n objects---> n times NSV's are initlized 

"""

class sample: 
    x=10
    y=20
    def m1(self): #method always should have self as a parameter 
        print(sample.x) #whichever object calls this display method then that object is sorted by self 
        print(sample.y) #accessing static variable using classname 

#end of class 
#to access the class members, we need to create object 
# objectname = classname()
s1=sample() #object create stmt --> here object is created internally and its address 
            #is stored in a variable variable called as reference variable(s1)

#now call the method using object 
s1.m1()
print(sample.x) #now accesing static variable from outiside the class using classname 