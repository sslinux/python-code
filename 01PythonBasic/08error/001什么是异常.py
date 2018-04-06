# 原本程序中出现的错误，异常表现；

# 当python检测到一个错误时，解释器就无法继续执行了，这时会终止程序的执行，并打印错误信息。这就是异常;


try:                 # 尝试执行可能出现错误的代码：
    # 11/0
    # open("xxx.txt")
    # print(num)
    print("----1----")
except NameError:    # 可能出现的错误； py2中这里可以用逗号分隔多个；py3中使用(NameError,FileNotFoundError)的方式；
    print("如果捕获到异常后做的 处理...")    # 针对出现错误时执行的操作；
except FileNotFoundError:
    print("文件不存在")
except Exception as ret:    # Exception：所有异常的总称；
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常，这个except一定会捕获到。")
    print(ret)
else:
    print("没有异常才会执行的功能。")
finally:
    print("-----------finally-------------")    # 不管产生异常与否，都要执行；
print("---end---")  # 这一行和异常处理没关系；

