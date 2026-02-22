#Multi-Level Inheritence: Derived a class from another derived class

m=40 
class A: 
    x=10
    y=20 
    print(m)
    def m1(self):
        global m #froward declaration 
        m=50 
        print(m)
        print(A.x)
        print(A.y)

class B(A): 
    z=30 
    def m2(self):
        global m 
        m=60 
        total = B.x+B.y+B.z 
        print(total)
        print(m)

class C(B):
    def m3(self):
        avg=(C.x+C.y+C.z)/3 
        print(avg)
        print(m)

c1=C()
c1.m1()
c1.m2()
c1.m3()
#print("total", c1.total) #C' object has no attribute 'total'

b1=B()
b1.m1()
b1.m2()

print("\n\n")

print(A.__base__)
print(B.__base__)
print(C.__base__)

b1=B()
b1.m1()
b1.m2()