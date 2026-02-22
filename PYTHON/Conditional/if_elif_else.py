"""
Types of Conditional Statements in Python
1. if statement
2. if...else statement
3. if...elif...else statement
4. Nested if statement
5. pass statement
"""

# Example1: if statement
test = [10,20,30,40,50]
if 10 in test:
    print('yes')
else:
    print('no')

x = 10
if x > 5:
    print('yes')
else:
    print('no')

if x == 5:
    print('yes')
else:
    print('no')

name = 'samarium'
if name:
    print('name is not empty')
else:
    print('name is empty')

a = True
if a:
    print('a is true')
else:
    print('a is false')

nums = [1,2,3,4,5]
if x % 2 ==0:
    print('even numbers')
else:
    print('odd numbers')

is_raining = True
if is_raining:
    print('take umbrella')
else:
    print('no need to take umbrella')

value = None
if value:
    print('has value')
else:
    print('no value')

# if-elif-else statement
marks = 70
if marks >= 90:
    print("A grade")
elif marks >=60:
    print("B grade")
elif marks >=40:
    print("C grade")
else:
    print("Fail")

day = 'Monday'
if day == 'Monday':
    print("working day")
elif day == 'Tuesday':
    print("working day")
elif day == 'Wednesday':
    print("working day")
else:
    print("weekend")

# Nested if statement
age = 51
if age >= 18:
    if age <= 50:
        print("Eligible to work")
    else:
        print("Too old to work")
else:
    print("Not eligible to work")

username = 'admin'
password = 'admin123'

if username == 'admin':
    if password == 'admin123':
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown user")

# Logical operations
age = 25
if age > 18 and age < 60:
    print("Eligible to work")
else:
    print("Not eligible to work")

if username == 'admin' and password == 'admin123':
    print("Login successful")
else:
    print("Login failed")

# Membership operations
nums = [1,2,3,4,5]
if 3 in nums:
    print("3 is in the list")
else:
    print("3 is not in the list")

if 6 not in nums:
    print('not present')
else:
    print('present')

# Identity operations
a = 10
if a is None:
    print("a is None")
else:
    print("a is not None")

# Ternary operator
x = 15
result = 'Even' if x % 2 == 0 else 'Odd'
print(result)

# Conditonal with Loops
for i in range(10):
    if i == 8:
        print('Breaking the loop at', i)
        break
print(i)

for i in range(11, 20):
    if i == 15:
        print('Skipping', i)
        continue
print(i)

# Condtional with Functions
def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
obj = check_even(4)
print(obj)

def login(user, pwd):
    if user == 'admin' and pwd == 'admin123':
        return 'Login successful'
    else:
        return 'Login failed'

print(login('admin', 'admin123'))

















































