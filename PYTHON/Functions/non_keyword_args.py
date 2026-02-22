# *args (Non-keyword Arguments)

def fun1(*args):
    for args in args:
        print(args)

fun1(10, 20, 30, 40, 50)
fun1('samarium', 'bromine', 'lithium')
fun1(10, 'hello', 20.5, True)
