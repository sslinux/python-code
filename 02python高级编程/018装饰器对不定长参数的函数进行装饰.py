"""
使用装饰器对不定长参数的函数进行装饰
"""

def func(funcName):
    # print("---func---1---")

    def func_in(*args,**kwargs):
        print("---func_in---1---")
        funcName(*args,**kwargs)
        print("---func_in---2---")

    # print("---func---2---")
    return func_in 

#test = func(test)
@func
def test(a,b,c):
    print("---test1---a=%d,b=%d,c=%d---"%(a,b,c))

@func
def test2(a,b,c,d):
    print("----test2---a=%d,b=%d,c=%d,d=%d---"%(a,b,c,d))

test(11,22,33) 
test2(44,55,66,77)