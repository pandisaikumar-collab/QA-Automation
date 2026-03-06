"""
Multi-processing: Running multiple processes at the same time, where each
                 process has its own memory and CPU execution

A process is completely independent
"""

import multiprocessing

def numbers():
    for i in range(5):
        print(i)

def letters():
    for ch in ['a','b','c','d','e']:
        print(ch)

p1 = multiprocessing.Process(target=numbers)
p2 = multiprocessing.Process(target=letters)

p1.start()
p2.start()


