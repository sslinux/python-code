a = 100

def test():
    a = 200    # 函数中的局部变量与全局变量名称相同时，在函数中，使用的是局部变量；
    print("a=%d"%a)

def test2():
    print("a=%d"%a)

test()
test2()