"""
> import argparse
> argparse is used to take input from the command line
> it makes our script easy to use and professional

how to run:
python test.py --name Sai
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name')
args = parser.parse_args()
print('hello', args.name)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--user")
parser.add_argument("--role")
args = parser.parse_args()

print(args.user, "is", args.role)
# python test.py --user Sai --role Admin
