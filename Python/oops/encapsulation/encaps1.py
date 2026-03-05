
# Encapsulation: Combine variables + methods inside a class
# Hide sensitive data using private variables (__variable)


class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary   # private variable

    def show(self):
        print(self.name)
        print(self.age)
        print(self.__salary)

    def get_salary(self):
        return self.__salary


emp_obj = Employee("Sai", 20, 1000)

emp_obj.show()

print(emp_obj.name)

# print(emp_obj.__salary) will give error because pvt
print(emp_obj.get_salary())