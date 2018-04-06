"""
集合set：

    集合与之前列表、元组类似，可以存储多个数据，但是这些数据是不重复的
    集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric_difference(对称差集)等数学运算.
"""

"""
In [1]: x = set('abcd')

In [2]: x
Out[2]: {'a', 'b', 'c', 'd'}

In [3]: type(x)
Out[3]: set

In [4]: y = set(['h','e','l','l','0'])

In [5]: y
Out[5]: {'0', 'e', 'h', 'l'}

In [6]: z = set('spam')

In [7]: z
Out[7]: {'a', 'm', 'p', 's'}

In [8]: y & z  # 交集
Out[8]: set()

In [9]: x & z  # 交集
Out[9]: {'a'}

In [10]: x|y   # 并集
Out[10]: {'0', 'a', 'b', 'c', 'd', 'e', 'h', 'l'}

In [11]: x-y   # 差集
Out[11]: {'a', 'b', 'c', 'd'}

In [12]: x^y   # 对称差集(在x中或在y中，但不会同时在两个集合中)
Out[12]: {'0', 'a', 'b', 'c', 'd', 'e', 'h', 'l'}

In [13]: len(x)
Out[13]: 4

In [14]: len(y)
Out[14]: 4

In [15]: len(z)
Out[15]: 4
"""
