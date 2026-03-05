# by using decorator we can add additional functionality to the existing fun
# without changing the behavior


def decorator_fun(func):
    def wrapper():
        print('before calling')
        func()
        print('after calling')

    return wrapper


@decorator_fun
def m1():
    print('metho1')

@decorator_fun
def m2():
    print('metho2')


m1()
m2()