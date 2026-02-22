#super(): This stmt is used  to call super class methods or constructor through 
#subclass method or constructor

class A: 
    def __init__(self):
        print('form constructor A...')
        self.x = 10 

class B(A):
    def __init__(self):
        print('constructor from class B')
        super().__init__() #executes super class constructor 
        self.y=20 
        print(self.x)
        print(self.y)


b1 = B()

#here first super class constructor executes followed by subclass constructor
#here both logics are executed predefined logic(derived class logic) and base class logic

