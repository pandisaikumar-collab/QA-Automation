# whe to use sys module
# script is very small, quick testing, no validation needed
# it is list, by default first element is the script name
# Example usage: python sys_fun.py arg1 arg2 arg3

import sys
print(sys.argv)
print('File name: ', sys.argv[0])
print('Length of arguments: ', len(sys.argv))
#print("First value:", sys.argv[1])

