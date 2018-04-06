"""
通用装饰器，包含参数和返回值
"""

def func(funcName):
    def func_in(*args,**kwargs):
        print("---记录日志---")
        value = funcName(*args,**kwargs)
        return value

    return func_in 

@func
def test():
    print("---test---")
    return "haha"

@func 
def test2():
    print("---test2---")

def test3(a):
    print("---test3--a=%d"%a) 

ret = test() 
print("test retuan value is %s:"%ret) 

a = test2()
print("test2 return value is %s"%a)

test3(11)