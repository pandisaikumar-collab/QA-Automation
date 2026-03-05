#Destructor: whenever a object gets removed, destructor will be executed automatically 
#Destructor is defined always suing the name __del__ 
#Destructor will be executed automatically whenever a object gets removed,
#we no need to call.

class test:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("destructor called")

t1=test() #RC1
t2=test() #RC1
t3=test() #RC1 

print(t3)
t4=t3

t3=test() 
#if same ref variable is used, then RC of previous t3 decreases by 1 
#RC=0 (if same variable is used, RC becomes less 0)
#previous t3 object is removed and destructor executed 
#and a new t3 object is created 

print(t3)

