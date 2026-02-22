# Accessing NSV of super class constructor from subclass constructor
# using super 

class A: 
    def __init__(self):
        self.x=10 
        print('from class A...')

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20 


b1 = B()
a1 = A()
print(b1.x)
print(b1.y) #now you can be accessed 

