
#Hierarchicla Inheritence: A base class with multiple derived classes 

class Arith: 
    x=20 
    y=30 
    def m1(self):
        print(Arith.x)
        print(Arith.y)

class Add(Arith):
    def m2(self):
        res_sum = Add.x+Add.y 
        print(res_sum)

class Sub(Arith):
    def m3(self):
        res_sub = Sub.x-Sub.y 
        print(res_sub)

class Mul(Arith):
    def m4(self):
        res_mul = Mul.x*Mul.y 
        print(res_mul)

class Div(Arith):
    def m5(self):
        res_div = Div.x/Div.y 
        print(res_div)

a1=Add()
a1.m2()

s1=Sub()
s1.m3()

m1=Mul()
m1.m4()

d1=Div()
d1.m5()

print(Div.__base__)
print(Mul.__base__)
print(Sub.__base__)
print(Add.__base__)

print(Add.__mro__)