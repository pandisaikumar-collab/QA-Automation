"""
Encapsulation:
> Means keeping data safe inside a class and controlling
 how it is accessed or modified from outside the class.
    - bundle data + method together
    - you hide internal details (variables)
    - you can control access using methods (getters/setters)
    - Focus: how data is stored and protected
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

acc = BankAccount(100)
print(acc.get_balance())
#print(acc.__balance)  # Error: can't access private variable
#internal data is hidden and protected
#access only through methods


"""
Abstraction:
> Means showing only what is necessary and hiding how it works.
> Only important details are shown to the user.
> Complexity is hidden.
> Focus: what an object can do, not how it dose it.
> Hide how things work internally and show only required functionality.

Note:
*****
Encapsulation: Battery/circuits/chips are hidden inside the phone
                you can't access them directly, but you can use methods 
                (buttons/apps)
                * Hide DATA
                * Hides internal data and provides controlled access 
                  using methods 

Abstraction: You see only the phone interface buttons/apps
             you don't know internal workings of circuits/chips
             * Hide LOGIC
             * Hides implementation details and 
               exposes only required functionality

In encapsulation, access is blocked
In abstraction, access is not part of the design
"""



































