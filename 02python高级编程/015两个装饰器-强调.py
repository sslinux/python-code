def w1(func):
    print("---正在装饰1---")
    def inner():
        print("---正在验证权限1---")
        func()  
    return inner

def w2(func):
    print("---正在装饰2---")
    def inner():
        print("---正在验证权限2---")
        func() 
    return inner

@w1
@w2
def f1():
    print("---f1---")

f1()   