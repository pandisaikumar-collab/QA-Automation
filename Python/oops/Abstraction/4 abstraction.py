class sample:
    __x=100
    def m1(self):
        self.__y=200
        print(sample.__x)
        print(self.__y)


s1 = sample()
s1.m1()
#print(__x)
# print(sample.__x)
# print(self.__y)