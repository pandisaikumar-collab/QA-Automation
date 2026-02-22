#parameterezed constructor 
#constructor with parameters is called as parameterized constructor 

class Test:
    def __init__(self, a, b): #constructor with parameters 
        self.x=a
        self.y=b 
    
    def m1(self,p,q):
        r=p+q #local variable sum 
        s=self.x+self.y #sum of NSV's 
        print(r)
        print(s)

t1=Test(10,20)
t1.m1(100,200)


