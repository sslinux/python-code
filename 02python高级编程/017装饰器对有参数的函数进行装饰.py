"""
使用装饰器对有参数的函数进行装饰
"""

def func(funcName):
    # print("---func---1---")

    def func_in(a,b):
        print("---func_in---1---")
        funcName(a,b)
        print("---func_in---2---")

    # print("---func---2---")
    return func_in 

#test = func(test)
@func
def test(a,b):
    print("---test-a=%d,b=%d---"%(a,b))

test(11,22) 