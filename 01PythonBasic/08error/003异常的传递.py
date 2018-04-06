def test1():
    print("---test1-1---")
    print(num)
    print("---test1-2---")

def test2():
    print("---test2-1---")
    test1()
    print("---test2-2---")

def test3():
    try:
        print("---test3-1---")
        test1()
        print("---test3-2---")
    except Exception as result:
        print("捕获到了异常，信息是:%s"%result)
    
    print("---test3-2---")

test3()    # test1()并没有异常处理的代码，但它发生异常时可以向调用它的地方传递，由test3()中的代码来处理；
print("---华丽的分割线---")
test2()    # test2()中也没有异常处理代码，所以调用test1()是产生的异常最终传递给了python解释器，导致中断程序，打印错误信息；