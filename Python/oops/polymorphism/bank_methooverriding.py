# ex method overriding 
# inheritance + method overriding
# type is single inheritance

class RBI: 
    x=10 
    def minbalance(self):
        minbal = 0 
        print('RBI MINBAL: ', minbal)

class HDFC(RBI): #here minimal=1000, I won't RBI minimal here, so i docent want super class
    def minbalance(self): #logic to execute, so I override the method so that subclass
        minbal=1000       #method logic execute 
        print('HDFC MINBAL', minbal)

class ICICI(RBI):
    x=100 
    def minbalance(self): 
        minbal=2000 
        print('ICICI MINBAL :', minbal)

class SIB(RBI):
    x=10 
    pass #here it doesn't want to override, it will follow RBI rules only
         #here it will execute super class method logic only 

h1=HDFC()
h1.minbalance()

i1=ICICI()
i1.minbalance()

s1=SIB()
s1.minbalance()

print(RBI.x)
print(ICICI.x)
print(SIB.x)
