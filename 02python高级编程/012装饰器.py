"""
装饰器： 如虎添翼，是python的语法糖。
"""


# 函数名重名：
# def test1():
#     print("---1---")
# def test1():
#     print("---2---")

# test(1)   # 打印的是2



# 开放封闭原则：已经实现的功能代码不允许被修改，但可以扩展；
# 封闭： 已实现的功能代码块；
# 开放： 对扩展开发；

# 语法糖：装饰器


def w1(func):
    def inner():
        print("---正在验证权限---")
        func()
    return inner 

def f1():
    print("---f1---")

def f2():
    print("---f2---")

# innerFunc = w1(f1)   # 将函数对象f1作为参数传递给w1,func接收；返回inner函数给innerFunc；
# innerFunc()   # 但此时，调用f1或f2的方式方式了变化，需要使用innerFunc来调用了；不合理；

f1 = w1(f1)
f1()     # 调用方式没变，但现在的f1,指向的是闭包中的inner()。