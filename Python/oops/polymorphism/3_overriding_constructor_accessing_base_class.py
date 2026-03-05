class A:
    def __init__(self):
        self.x=10 
        print('from constructor A...')

class B(A):
    def __init__(self):
        self.y=20 
        print('from constructor B...')


a1=A()
print(a1.x)

b1=B()
print(b1.y)

#print(b1.x) #invalid, becoz constructor overriden, here x is not initialized 

#in constructor overriding, we cannot access base class NSVs 
#in constructor overrding, using derived class object access accessing both base and derived class NSV's 
#for that the so