#program = local/global/static/non-static/global

x=10 #gbv
class test:
    y=20 #sv
    def display(self,p): #lc
        self.z=p 
        self.w=x+test.y+self.z+p 
        print(x)
        print(p)
        print(test.y)
        print(self.z)
        print(self.w)

t1=test()
t1.display(50)


