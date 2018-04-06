
def test(a,b,c=33,*args,**kwargs):
    print(a) # 打印第1个位置参数；
    print(b) # 打印第2个位置参数；
    print(c) # 打印第3个位置参数，如果调用时未传递，则使用默认值；
    print(args) # 接收剩余的位置参数，组成一个集合;
    print(kwargs) # 接收剩余的关键字参数，组成一个字典；

A = (44,55,66)
B = {"name":"laowang","age":18}

test(11,22,33,*A,**B)   # 拆包，也叫参数解包，*拆元组，**拆字典；



