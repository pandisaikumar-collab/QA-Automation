
#subclass method calling super class method

class A: 
    def m1(self):
        self.x = 10 
        print(self.x)

class B(A):
    def m2(self):
        super().m1() 
        self.y = 20 
        print(self.y)

b1 = B()
b1.m1()

#for overriding and executing predefined logic only, no need of super,
#but to executed pre-defined logic and user-defined logic, we need super 

