#working with static, local and global 
#global variables------> defined outside the class 
#local variables-------> defined within the class and within the methods 
#static variables -----> defined within the class and outside the methods 

r=30 #global var
class demo:
    x=10
    y=20 #sv 
    print(x)
    print(y)
    print(r)
    def compute(self, p, q):
        #modify a global variable 
        global r #forward declaration 
        z=p+q+r #p,q,z are local variables, here sum of local and global variables. 
        w=demo.x+demo.y 
        print(z)
        print(w)
        print(r)

d1=demo()
d1.compute(40,50)

