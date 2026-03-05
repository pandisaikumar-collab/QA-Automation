class sample:
    def __init__(self):
        self.x=10
        self.y=20
    def m1(self):
        self.x=self.x+30
        self.y=self.y+40
        print(self.x)
        print(self.y)

s1=sample()
s1.m1()

print(s1.x)
print(s1.y)


s2=sample()
s2.m1()

print(s2.x)
print(s2.y)