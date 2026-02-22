class sample:
    a=10
    def display(self,p,q):
        r=70 #local varibles 
        self.x=20 #NSV 
        self.y=30
        print(p)
        print(q)
    
    def show(self):
        print(sample.a)
        print(self.x)
        print(self.y)
        res_sum = self.x+self.y+sample.a
        print(res_sum)


s1=sample()
s1.display(100,200)  #s1 address will be stored in self of display 
s1.show()

