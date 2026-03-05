from abc import ABC
from abc import abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate(self, *args):
        pass


class FullTimeEmployee(Employee):

    def calculate(self, salary):
        return salary * 10


class PartTimeEmployee(Employee):
    def calculate(self, hours, rate):
        return hours * rate


full_obj = FullTimeEmployee()
print(full_obj.calculate(100))

part_obj = PartTimeEmployee()
print(part_obj.calculate(10, 200))

# cannot create directly Employee obj and can't call calculate method since hiding implementation
# emp_obj = Employee()
# print(emp_obj.calculate(10, 200))

