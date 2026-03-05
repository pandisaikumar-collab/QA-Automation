
def test_kwargs(**kwargs):

    res_dict = {}
    for key,value in kwargs.items():
        res_dict.update({key:value})

    return res_dict

print(test_kwargs(a=1, b=2, c=3))