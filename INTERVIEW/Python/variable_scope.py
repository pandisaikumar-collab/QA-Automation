"""
Variable Scope:
 > Variable scope means:
   (where a variable can be used and where it cannot be used)
   (inside a class, variable have different scope (levels))

Types of variable scope inside a class:
    1. Instance Variable Scope
    2. Class Variable Scope
    3. Local Variable Scope

Instance Variable Scope:
    > belong one object(instance) of a class
    > created using self
    > each object has its own copy of instance variable
    > can access using self or object name
    > can be accessed anywhere inside the class using self or object name
    > cannot be accessed outside the class using class name

Class Variable Scope:
    > belong to the class
    > shared by all objects of the class
    > created without self
    > defined inside the class but outside the methods
    > can be accessed using class name or self
    > can be accessed anywhere inside the class using class

Local Variable Scope:
    > create inside a method
    > used only inside that method
    > Not stored in the object or class
    > cannot be accessed outside the method

"""
# Instance Variable Scope Example:
class A:
    def __init__(self, value):
        self.instance_var = value  # instance variable

obj1 = A(10)
obj2 = A(20)
print(obj1.instance_var)  # 10
print(obj2.instance_var)  # 20
#print(self.instance_var) # Error
#print(A.instance_var)     # Error

# Class Variable Scope Example:
class B:
    company_name = "TCS"
    def show(self):
        print(self.company_name)
        print(B.company_name)

obj = B()
obj.show()
print(B.company_name)
print(obj.company_name)
#print(self.company_name) # Error

# Local Variable Scope Example:
class C:
    def display(self):
        local_var = "Local Variable"
        print(local_var)
        #print(self.local_var) # Error

c1 = C()
c1.display()
#print(c1.local_var) # Error
#print(C.local_var)  # Error


# All variables together:
class Demo:
    class_var = "Class Variable"

    def __init__(self, name):
        self.instance_name = name # instance variable

    def show(self):
        local_var = 50  # local variable
        print("Local Variable:", local_var)
        print("Instance Variable:", self.instance_name)
        print("Class Variable:", Demo.class_var)

d1 = Demo('Kumar')
d1.show()
print(Demo.class_var)
print(d1.instance_name)
#print(d1.local_var) # Error
#print(Demo.local_var) # Error
#print(self.class_var) # Error
#print(self.instance_name) # Error
#print(self.local_var) # Error













