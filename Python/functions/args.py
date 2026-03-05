# by using args we can pass number of parameters
def test_args(*args):

    res_list = []
    for arg in args:
        res_list.append(arg)
    return res_list


print(test_args('a', 'b', 1, 2, 3))