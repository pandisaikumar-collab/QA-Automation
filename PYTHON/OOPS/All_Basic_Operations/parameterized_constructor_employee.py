class employee:
    """ Employee Application """
    company='Infosys'
    empcount=0 
    def __init__(self, empname, empid, empsal, design='SE', *launguages, **details):
        #howmany constructor parameters are defined, those many 
        #NSV's should be defined 
        self.empname=empname
        self.empid=empid
        self.empsal=empsal 
        self.design=design
        self.launguages=launguages 
        self.details=details 
        employee.empcount=employee.empcount+1 
    
    def displayemployee(self):
        print('EMPLOYEE NAME: ', self.empname)
        print('EMPLOYEE ID: ', self.empid)
        print('EMPLOYEE SALARY: ', self.empsal)
        print('EMPLOYEE DESGINATION: ', self.design)
        print('LAUNGUAGS :', self.launguages)
        print('DETAILS :', self.details)

emp1=employee('mark', 10, 100000, 'MANAGER', 'ENG', 'HINDI', grade='A', age=25)
emp1.displayemployee()

    
