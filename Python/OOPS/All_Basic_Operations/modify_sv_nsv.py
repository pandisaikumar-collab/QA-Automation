#program for modifying static and non-static variable

class sample:
    a=4.5
    b=5.5 
    def display(self):
        self.x=10
        self.y=20
        print(self.x)
        print(self.y)
        print(sample.a)
        print(sample.b)
    
        #modifying the values 

        self.x=100
        self.y=200
        sample.a=50 
        sample.b=100

        print(self.x)
        print(self.y)
        print(sample.a)
        print(sample.b)

s1=sample()
s1.display()

s2=sample()
s2.display()