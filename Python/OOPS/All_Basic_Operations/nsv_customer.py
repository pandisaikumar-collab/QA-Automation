class Customer:
    ''' CUSTOMER APPLICATION'''

    def getDetails(self):
        self.cname = input('Enter customer name: ')
        self.accno = int(input("Enter customer accont no: "))
        self.address = input("Enter customer address: ")
        self.balance = int(input("Enter customer balance: "))
    
    def putDetails(self):
        print('Customer Name: ', self.cname)
        print('Customer Account num: ', self.accno)
        print('Customer Address: ', self.address)
        print('Customer Balance: ', self.balance)
    
    def deposit(self):
        self.damout = int(input('Enter deposit amoutn: '))
        self.totalamount = self.damout + self.balance
        print('Total balance is: ', self.totalamount)
    
    def withdraw(self):
        self.wamount = int(input("Enter withdraw amount: "))
        self.totalamount = self.totalamount - self.wamount 
        print('Total amount: ', self.totalamount)

c1=Customer()
c1.getDetails()
c1.putDetails()
c1.deposit()
c1.withdraw()


c2=Customer()
c2.getDetails()
c2.putDetails()
c2.deposit()
c2.withdraw()