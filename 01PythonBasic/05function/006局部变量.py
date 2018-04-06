def test1():
    a = 100   # 变量a只能在该函数内使用，任何外部试图调用它都会引发异常；

def test2():
    # print("a=%d"%a)   # 报错，因为a未定义；
    pass

test1()
test2()
