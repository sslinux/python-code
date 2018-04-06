# 调用函数时，缺省参数的值如果没有传入，则被认为是默认值。

def test(a,b=22):   # 缺省参数只能放在最后；
    result = a+b 
    print("result=%d"%result)

test(11)
test(33,33)   # 若给默认参数传值了，则使用传递过去的值；
test(44)  



def test2(a,b=22,c=33):   # 定义时使用=，表示是缺省参数；
    print(a)
    print(b)
    print(c)

test2(11,c=44)  # 调用时使用=，叫做命名参数；

