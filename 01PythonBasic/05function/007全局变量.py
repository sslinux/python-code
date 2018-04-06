# 全局变量：仅在当前模块文件中的全局；

a = 100  # 全局变量；
def test1():
    print("a=%d"%a)

def test2():
    print("a=%d"%a)

test1()
test2()

