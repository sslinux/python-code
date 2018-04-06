# 全局变量：定义在函数外，一定要定义在调用之前；

a = 100
def test():
    print("a=%d"%a)
    print("b=%d"%b)
    # print("c=%d"%c)

b = 200

test()

# c = 300   # 在此处定义是不行的，因为在函数调用之后；