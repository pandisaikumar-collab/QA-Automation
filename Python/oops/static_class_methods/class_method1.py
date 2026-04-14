class Employee:
    company = 'cisco'

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def show(self):
        print(self.name)
        print(self.age)
        print(self.__salary)
        print(self.company)
        print(Employee.company)

    def get_salary(self):
        return self.__salary

    @staticmethod
    def is_adult(age):
        return age >= 18
        # using when login is related to class
        # but dose't need self or cls
        # utility function inside class

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


emp_obj = Employee('sai', 25, 10000)
emp_obj.show()
emp_obj.get_salary()
print(emp_obj.name)
print(Employee.is_adult(20))
print(emp_obj.is_adult(16))
Employee.change_company('Google')  # now compnay becomes google for all objects
print(Employee.company)








