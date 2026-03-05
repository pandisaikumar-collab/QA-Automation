"""
Polymorphism 
Means (many forms)

Different classes can define methods with the same name,
and python can call the appropriate method depending on the object 
without knowing it's exact class.
"""

## Method overriding (True polymorphism)

class A: 
    def m1(self):
        print("m1 method from class A..")

class B(A):
    def m1(self): #overriding parent method 
        print("m1 method from class B..")
        super().m1() #to call parent method inside child class 

class C(B):
    def m1(self):
        print("m1 method from class C..")

#* code fails because (TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B)
# class C(A,B):
#     def m1(self):
#         print("m1 method from class C..")
        

# for a in [A(), C(), B()]:
#     a.m1()

# this is runtime polymorphism: the method m1() behaves differently 
# based on the object 

c1 = B()
c1.m1()


"""
MRO (Method Resolution Order)
MRO is the order in which python looks for a method or attribute in a class hierarchy.
In Multiple inheritance, python follows a specific order to resolve method 
    to avoid ambiguity.
Python uses the C3 Linearization algorithm to determine this order
"""



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()


print(C.__mro__)





