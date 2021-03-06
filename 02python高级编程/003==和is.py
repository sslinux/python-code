# == 判断值是否相等；
# is 判断指向的对象是否是同一个；

# In [1]: a = [11,22,33]

# In [2]: b = [11,22,33]

# In [3]: c = a

# In [4]: id(a),id(b),id(c)
# Out[4]: (140019021946952, 140019022059720, 140019021946952)

# In [5]: a == b
# Out[5]: True

# In [6]: a is b
# Out[6]: False

# In [7]: a == c
# Out[7]: True

# In [8]: a is c
# Out[8]: True


# 数字有特殊情况:
# Python会对比较小的对象缓存，下次用到比较小的对象时，会去缓存区查找，如果找到，不会再开辟新的内存，而是继续把小对象的地址赋给新的值。例子：
# In [9]: a = 100

# In [10]: b = 100

# In [11]: a == b
# Out[11]: True

# In [12]: a is b
# Out[12]: True

# In [13]: a = 10000

# In [14]: b = 10000

# In [15]: a is b
# Out[15]: False

# 对于字符串，你可以通过使用intern函数强制使用缓存区。