#Default constructor 

class sample:
    def __init__(self): #constructor 
        print("constructor of sample class")
        self.x=10 
        self.y=20 
    
    def display(self):
        print("Method of sample class")
        print(self.y)
        print(self.y)

s1=sample() #whenever object created, immediately constructor gets executed automatically 
s1.display()
s1.display()
s1.display() #method called multiple times. 
print(s1.x)
print(s1.y)