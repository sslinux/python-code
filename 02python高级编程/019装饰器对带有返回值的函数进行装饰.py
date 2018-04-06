"""
使用装饰器对有返回值函数进行装饰
"""

def func(funcName):
    print("---func---1---")

    def func_in():
        print("---func_in---1---")
        value = funcName()     # 保存返回来的"haha"
        print("---func_in---2---")
        return value   # 把"haha"返回到调用处;

    print("---func---2---")
    return func_in 

@func
def test():
    print("---test---")
    return "haha"

ret = test() 
print("test retuan value is %s:"%ret) 