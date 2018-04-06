# 匿名函数作为参数传递：

# def test(a,b):
#     result = a + b
#     return result

# num = test(11,22)
# print(num)


# 匿名函数扩展：
# def test(a,b,func):
#     result = func(a,b)
#     return result 

# num = test(11,22,lambda x,y:x+y)
# print(num)


def test(a,b,func):
    result = func(a,b)
    return result

# 适用于py2
# func_new = input("请输入一个您名函数.")   

# 适用于py3：
func_new = input("请输入一个匿名函数:")
func_new = eval(func_new)   # eval转换为表达式；

num = test(11,22,func_new)
print(num)


# 由此证明，python是一个动态语言；
