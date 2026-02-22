#hidding static and NSV 

class sample:
    __x=100 #hiding 
    def display(self):
        self.__y=200 #hiding NSV 
        print(sample.__x)
        print(self.__y)

s1 = sample()
s1.display()

# print(sample.__x) #S.V can't b accessed 
# print(s1.__y) #NSV cant be accessed 

