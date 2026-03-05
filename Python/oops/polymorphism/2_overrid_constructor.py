
class x:
    def __init__(self, a, b):
        print("from constructor of x...")
        self.a = a 
        self.b = b 
    
class y(x):
    pass 
    # def __init__(self):
    #     print("from constructor of y...")

# y1=y()
# print(y)
y2=y(3,4)
#x1=x(10,20,30)

#constructor overloading happens----->error