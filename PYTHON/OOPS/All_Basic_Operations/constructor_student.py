class student:
    def __init__(self):
        self.name=input("Enter student name :")
        self.rollno=int(input("Enter student rollno :"))
        self.branch=input("Enter student branch: ")
        self.rank=int(input("Enter rank: "))
    
    def display(self):
        print('NAME :', self.name)
        print('ROLLE NO: ', self.rollno)
        print('BRANCH ', self.branch)
        print('RANK: ', self.rank)

print('Enter student1 details: ')
s1=student()
s1.display()

print('Enter student2 details: ')
s1=student()
s1.display()