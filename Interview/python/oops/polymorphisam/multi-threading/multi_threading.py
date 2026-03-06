"""
Multi-threading: Running multiple task at the same time inside a programm
                 using threads.

"""
import time
import threading

class A:

    def numbers(self):
        for i in range(10):
            print(i)
            time.sleep(0.1)

    def letters(self):
        for ch in ['a', 'b', 'c', 'd', 'e']:
            print(ch)
            time.sleep(0.1)

a1  = A()

t1 = threading.Thread(target=a1.numbers)
t2 = threading.Thread(target=a1.letters)

t1.start()
t2.start()

