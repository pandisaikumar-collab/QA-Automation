# if the base classes have method with same name and using derived class object 
# if you access the method then which base class method will executed ?

class A: 
    x=10
    y=20 
    def m1(self):
        print("m1 method from class A...")
        print(A.x)
        print(A.y)

class B:
    a=2.5 
    b=3.5 
    def m1(self):
        print("m1 method from class B")
        print(B.a)
        print(B.b)

class C(A,B): #(B,A) #based on class args will execute 
    def m2(self):
        intsum = C.x+C.y 
        intfloat = C.a+C.b 
        print(intsum)
        print(intfloat)


c1 = C()
c1.m1()