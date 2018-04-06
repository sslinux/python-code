"""
使用装饰器对无参数的函数进行装饰
"""

def func(funcName):
    print("---func---1---")

    def func_in():
        print("---func_in---1---")
        funcName()
        print("---func_in---2---")

    print("---func---2---")
    return func_in 

@func
def test():
    print("---test---")

test() 