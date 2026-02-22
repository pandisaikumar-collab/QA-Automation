#Employee application to perform various operations such as 
#DA(), TA(), HRA(), PF(), TAX()

class employee(object):
    """
    Employee Application 
    """
    company='infosys'
    empcount=0
    def __init__(self, empname, empid, empsal, design):
        self.empname = empname
        self.empid = empid
        self.empsal = empsal
        self.design = design
    
    def da(self, daamt): #daily allowance 
        self.empsal = self.empsal + daamt
    
    def hra(self, hraamt): #hourse rent allowance
        self.empsal = self.empsal + hraamt 
    
    def ta(self, taamt): #traveling allowance
        self.empsal + self.empsal + taamt 

    def tax(self):
        if ((self.empsal> 25000) and (self.empsal<=5000000)):
            self.empsal=self.empsal-self.empsal*0.10 
            print('Salary after tax reduction = ', self.empsal)
        elif ((self.empsal > 50000 and (self.empsal<=100000))):
            self.empsal=self.empsal-self.empsal*0.15 
        elif (self.empsal>100000000):
            self.empsal=self.empsal-self.empsal*0.20 
    
    def displayemployee(self):
        print('NAME :', self.empname)
        print('ID: ', self.empid)
        print('SLARY :', self.empsal)
        print('DESIGNATION :', self.design)

emp1=employee('SAIKUMAR', 101, 100000, 'MANAGER')
emp1.displayemployee()
