# 函数也是一个对象：
"""
In [52]: def test():
    ...:     print("----1----")
    ...:     

In [53]: test
Out[53]: <function __main__.test>

In [54]: b = test    # b 和 test 指向了同一个函数体(对象)

In [55]: b
Out[55]: <function __main__.test>

In [56]: test()
----1----

In [57]: b()   # 调用b()和调用test()的效果是一样的；
----1----
"""


# def test(num):

#     print(number)

# test(100)


#######################################################################
# 函数闭包：

def test(num):
    print("---1---")

    def test_in(num_in):  # 在函数的内部又定义了一个函数；
        print("---2---")
        print(num+num_in) # 内部函数使用了外部函数的变量；

    print("---3---")
    return test_in  # 外部函数返回的是内部函数的引用；

ret = test(100)   # 调用外部函数时，内部函数不会被执行，只是将内部函数作为返回值返回；传递的参数会被内部函数保存；
# 因为ret指向了test函数中的 部分代码(test_in函数),所以test函数不会被销毁；

print("*"*30)
ret(1)          # 此时执行ret()函数就是在调用内部函数，并且内部函数中的变量num_in是1,num是调用外部函数时传递的100；
ret(100)        # 此时执行ret()函数就是在调用内部函数，并且内部函数中的变量num_in是100,num是调用外部函数时传递的100；
ret(200)        # 此时执行ret()函数就是在调用内部函数，并且内部函数中的变量num_in是200,num是调用外部函数时传递的100；

