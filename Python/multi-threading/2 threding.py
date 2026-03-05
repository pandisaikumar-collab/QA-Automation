import threading

class X:

    def m1(self):
        for i in range(1, 10):
            print(i)

    def m2(self):
        for j in range(11, 20):
            print(j)


x1 = X()

t1 = threading.Thread(target=x1.m1)
t2 = threading.Thread(target=x1.m2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Execution completed")