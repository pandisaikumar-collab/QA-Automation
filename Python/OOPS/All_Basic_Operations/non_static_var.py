"""
Non-static variables: The variables which are declared by using the name self are know 
                      as non-static variables or instance variables 

                      ex: self.x=10
                          self.y=20

non-static variables are alwyas defined within the methods

properties of Non-static variables:
===================================
1) if data is changing from one object to another object, then we can use non-static variables 
   ex: ename, eid, designation, salary

2) for all the non-static variables of a class, memory will be allocated for 
   multiple times, whenever we create a object 

   - for static variable, memory is allocated only once, 
   - but non-static variables, memory is allocated for 'n' no of times, depending on a no objects.

3) object is used ot allocate memory for non-static variable 
   em1=emp()
   emp1.ename='Miller' #e1 is the object which is allocating memory to NSV(ename)

   whenever object is created, that memoryalocation address of the object is taken 
   by python interpreter and create indirect address and this indirect address 
   is allocated to varible called reference variable(e1)
   ex: print(e1) -------> prints the address in-direct address of the object 

4) with respect to every object creation, seperate copy of memory will be allocated 
   allocated to non-static variables of the class. 
   ex: emp e1 will have its own data and methods
       emp e2 will have its own data and methods 

5) Non-static variables of a class can be accessed by all the methods 
   of the same class by using self. 

6) Non-static variables of one class can be accessed from outside 
   of that class by using reference variable and within the class
   by using self.
   
"""

