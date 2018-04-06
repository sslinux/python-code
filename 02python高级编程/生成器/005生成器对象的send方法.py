def test():
    i = 0
    while i<5:
        temp = yield i
        print(temp)      
        i+=1

t = test()  

# send方法的应用：

"""
In [12]: def test():
    ...:     i = 0
    ...:     while i<5:
    ...:         temp = yield i
    ...:         print(temp)      
    ...:         i+=1
    ...:         

In [13]: t = test()

In [14]: t.__next__()
Out[14]: 0

In [15]: t.__next__()
None
Out[15]: 1

In [16]: t.__next__()
None
Out[16]: 2

In [17]: t.send("haha")   # send方法和__next__方法一样能让生成器生成下一个对象，但不同是，send会传递一个参数去替代"yield i"的值；
haha
Out[17]: 3

In [18]: t.send("heihei")
heihei
Out[18]: 4
"""

# 注意：
# 1、生成器对象，生成第一个元素时，如果要使用send()方法，则需要使用send(None)的方式；
# 

"""
In [29]: def test():
    ...:     i = 0
    ...:     while i<5:
    ...:         if i == 0:
    ...:             temp = yield i
    ...:         else:
    ...:             yield i
    ...:         print(temp)      
    ...:         i+=1
    ...:         

In [30]: t = test()

In [31]: t.send(None)
Out[31]: 0

In [32]: t.send("haha")
haha
Out[32]: 1

In [33]: t.send("heihei")
haha
Out[33]: 2
"""