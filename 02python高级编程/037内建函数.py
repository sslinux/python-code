# range函数：

"""
py2中： range(INT)   返回一个列表；
py3中： range(INT)   返回一个生成器；

格式：range(Start,Stop,Step)
"""

# map函数：

"""
map函数会根据提供的函数对指定序列做映射.

map(...)
    map(function, sequence[, sequence, ...]) -> list

    function:是一个函数
    sequence:是一个或多个序列,取决于function需要几个参数
    返回值是一个list

**************************************************************
# 函数需要一个参数：
In [35]: for tmp in ret:
    ...:     print(tmp)
    ...:     
529

In [36]: ret = map(lambda x:x*x,[1,2,3])

In [37]: for tmp in ret:
    ...:     print(tmp)
    ...:     
1
4
9

************************************************************
In [38]: # 函数需要两个参数：

In [39]: ret = map(lambda x,y: x+y,[1,2,3],[4,5,6])

In [40]: for tmp in ret:
    ...:     print(tmp)
    ...:     
5
7
9

*******************************************************************
In [41]: def f1(x,y):
    ...:     return (x,y)
    ...: 

In [42]: l1 = [1,2,3,4,5,6,7]

In [43]: l2 = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

In [54]: weekday = list(week)

In [55]: weekday
Out[55]: 
[(1, 'Monday'),
 (2, 'Tuesday'),
 (3, 'Wednesday'),
 (4, 'Thursday'),
 (5, 'Friday'),
 (6, 'Saturday'),
 (7, 'Sunday')]

In [56]: d = dict(weekday)

In [57]: d
Out[57]: 
{1: 'Monday',
 2: 'Tuesday',
 3: 'Wednesday',
 4: 'Thursday',
 5: 'Friday',
 6: 'Saturday',
 7: 'Sunday'}

"""


# filter函数：

"""
filter函数会对指定序列执行过滤操作


    function:接受一个参数，返回布尔值True或False
    sequence:序列可以是str，tuple，list

filter函数会对序列参数sequence中的每个元素调用function函数，最后返回的结果包含调用结果为True的元素。

返回值的类型和参数sequence的类型相同
"""

"""
In [61]: ret = filter(lambda x: x%2,[1,2,3,4])

In [62]: for tmp in ret:
    ...:     print(tmp)
    ...:     
1
3
"""

# reduce函数：

"""
reduce函数，reduce函数会对参数序列中元素进行累积

reduce(...)
    reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.

    function:该函数有两个参数
    sequence:序列可以是str，tuple，list
    initial:固定初始值

reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function。 
第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial 作为参数调用function，否则会以序列sequence中的前两个元素做参数调用function。
注意function函数不能为None。

reduce(lambda x, y: x+y, [1,2,3,4])
10

reduce(lambda x, y: x+y, [1,2,3,4], 5)
15

reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd')
'ddaabbcc'
"""

# 在Python3里,reduce函数已经被从全局名字空间里移除了, 它现在被放置在fucntools模块里用的话要先引入： from functools import reduce

# ****************************************************************************************#
# sorted函数

"""
sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

In [64]: sorted([1,4,2,6,3,5])
Out[64]: [1, 2, 3, 4, 5, 6]

In [65]: sorted([1,4,2,6,3,5],reverse=1)
Out[65]: [6, 5, 4, 3, 2, 1]

In [66]: sorted(['dd','aa','cc','bb'])
Out[66]: ['aa', 'bb', 'cc', 'dd']

In [67]: sorted(['dd','aa','cc','bb'],reverse=1)
Out[67]: ['dd', 'cc', 'bb', 'aa']

"""