class sample:
    __x = 100  # private class variable

    def display(self):  # public method
        self.__y = 200  # private instance variable
        print(sample.__x)
        print(self.__y)
        self.display2()

    def display2(self):  # public method
        self.z = sample.__x + self.__y
        print(self.z)
        self.__display3()  # private method

    def __display3(self):  # private method
        self.a = 50
        print(self.a)

s1 = sample()
s1.display()
s1.display2()

#s1.__display3() 