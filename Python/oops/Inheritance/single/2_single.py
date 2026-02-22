# Program for single inheritance 
class A:
    x=10
    def m1(self):
        print("x=", A.x)

class B(A):
    y=20
    def m2(self):
        z=B.x+B.y 
        print("y=", B.y)
        print("z=", z)
b1=B()
b1.m1()
b1.m2()

print(B.__base__)
print(A.__base__)

#here B is derived class with a single base class A 