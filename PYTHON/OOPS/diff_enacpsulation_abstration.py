"""
Encapsulation:
==============
1. Encapsulation is the process of combining data variables and methods
2. it means putting data and functions together in single unit called class.
3. it hides the internal details of class from outside world.
4. so you can't change things directly from outside the class.
5. so this will protect data and keeps things organized.

Abstraction:
============
1. Abstraction is the process of hiding the implementation details and showing
   only functionality to the user.
2. it means showing only the important things and hiding the complicated details.

* so mainly different is that encapsulation is about bundling data and methods
  together, while abstraction is about hiding complexity and showing only
  essential features.

  Like encapsulation is hiding internal details of class, abstraction is hiding
    internal details of implementation.
"""
# Encapsulation example: (Keeps employee data safe inside the class)

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.__age = age
        self.__salary = salary

    def get_age(self):
        return self.__age

    def get_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary

emp1 = Employee('A', 20, 30000)
emp1.name = 'B'
print(emp1.name)
print(emp1.get_age())
emp1.get_salary(10000)
#print(emp1.__age) #AttributeError

# Abstraction example: (Hides complex implementation details)
from abc import ABC, abstractmethod
class  Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 'Full-time salary calculated'

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 'Part-time salary calculated'

ft = FullTimeEmployee()
print(ft.calculate_salary())

pt = PartTimeEmployee()
print(pt.calculate_salary())































