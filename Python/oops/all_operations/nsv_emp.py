class Employee:
    company="TCS"
    def getdetails(self):
        self.ename = input("Enter emplyee name: ")
        self.eid = int(input("Enter employee id: "))
        self.esal = int(input("Enter employee salary: "))
        self.edesignation = input("Enter employee designation: ")

    def putdetails(self):
        print("Ename: ", self.ename)
        print("Emid: ", self.eid)
        print("Emp sal: ", self.esal)
        print("Emp designation :",self.edesignation)
        print("Company: ", Employee.company)
        print(self)

e1=Employee()
e1.getdetails()
e1.putdetails()

e2=Employee()
e2.getdetails()
e2.putdetails()

