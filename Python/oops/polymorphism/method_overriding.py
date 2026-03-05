"""
Method Overriding:
    > same method name
    > same inputs
    > child class gives its own implementation

Execution:
    > python checks the child class first
    > if method found in child class, it executes
    > if method not found in child class, it checks parent class

Using Parent method also:
> super().show()

Rules:
> same method name
> same number of inputs
> child class must inherit parent class
> parent method is replaced

Need method overriding when:
> parent logic is not enough
> child needs different behavior
> we want custom behavior

Example:
    Parent - generic login
    child - admin login
"""
class Parent:
    def show(self):
        print("This is parent method.")

class Child(Parent):
    def show(self):
        super().show()
        print("This is child method.")

c1 = Child()
c1.show()

