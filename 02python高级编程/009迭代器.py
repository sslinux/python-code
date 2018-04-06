# 可迭代对象：
# 以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set，str等；
# 一类是generator，包括生成器和带yield的generator function 
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable. 

# 判断是否可以迭代：
# isinstance() 判断一个对象是否是Iterable对象：

# In [28]: from collections import Iterable

# In [29]: isinstance("abc",Iterable)   # isinstance判断"abc"是不是Iterable类的实例；
# Out[29]: True

# In [30]: isinstance([],Iterable)
# Out[30]: True

# In [31]: isinstance(100,Iterable)
# Out[31]: False


# 迭代器：
"""
可以被next()函数调用并不断返回下一个值的对象被称为迭代器:Iterator

可以使用instance() 判断一个对象是否是 Iterator 对象：

In [32]: from collections import Iterator

In [33]: isinstance((x for x in range(10)),Iterator)   # 生成器一定是迭代器；
Out[33]: True

In [34]: isinstance([],Iterator)
Out[34]: False

In [35]: isinstance({},Iterator)
Out[35]: False

In [36]: isinstance('abc',Iterator)
Out[36]: False

In [37]: isinstance(100,Iterator)
Out[37]: False

"""

# iter()函数
"""
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable对象 变成 Iterator可以使用iter()函数：

In [45]: isinstance(iter([]),Iterator)
Out[45]: True

In [46]: isinstance(iter('abc'),Iterator)
Out[46]: True

In [47]: a = "hello world"

In [48]: b = iter(a)

In [49]: next(b)
Out[49]: 'h'

In [50]: next(b)
Out[50]: 'e'

In [51]: next(b)
Out[51]: 'l'

"""