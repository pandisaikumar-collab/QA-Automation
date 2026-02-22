class cube:
    def __init__(self):
        self.length = int(input("Enter Length: "))
        self.breadth = int(input("Enter breadth: "))
        self.height = int(input("Enter height: "))
    
    def compute(self):
        self.volume = self.length*self.breadth*self.height
        print('VOLUME :', self.volume)

c1=cube()
c1.compute()