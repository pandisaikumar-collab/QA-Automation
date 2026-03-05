#program for non-static variables 

class sample:
    a=10
    b=20
    def display(self):
        self.x=30
        self.y=40
        print(sample.a)
        print(sample.b)
        print(self.x)
        print(self.y)

        #all methods can access the sv's and nsv's
    
    def show(self):
        print(sample.a)
        print(sample.b)
        print(self.x)
        print(self.y)

s1=sample()
s1.display()
s1.show()


#static variables related to class 
#non-static variables related to object 
#NSV can be accessed within the class using self 
#NSV can be accessed form outside the calss using object/ref.variables 
#SV can be accessed inside/outside the class using classname 


"""
1) how to defined NSV ---> wihtin the class within the method --> self 
2) how to access NSV within the class ---> self 
3) how to access NSV from outside the class ---> ref.variable/object  
4) who initalizes the NSV ----> object 
5) if there are 2 object, then how memory allocated to NSV ---> 2 
6) does every object has it's own NSV's -----> yes 

q) why NSV should be defined within the method ?
q) what happends if we define NSV outside the method ?
q) how NSV's and objects are related ?

Ans: 
    objec address------> passed to self of a method---> using that self only NSV are created 
    if NSV defined outside the method, the non-static variable cannot get the address of the object
    and NSV cannot be created.

"""