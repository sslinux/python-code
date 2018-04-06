"""
装饰器带参数;
应用：同一个装饰器，装饰不同的函数时，根据传递的值不同，进行判断处理；
"""

def func_arg(arg):
    def func(functionName):
        def func_in():
            print("---记录日志--arg=%s--"%arg)
            if arg == "heihei":
                functionName()
                functionName()
            else:
                functionName()

        return func_in 
    return func 

# 1、先执行func_arg("heihei")函数，这个函数return的结果是func函数的引用；
# 2、@func
# 3、使用@func对test进行装饰
@func_arg("heihei")
def test():
    print("---test---")

# 带有参数的装饰器，能够起到在运行时，有不同的功能；
@func_arg("haha")
def test2():
    print("---test2---")

test()
test2()

