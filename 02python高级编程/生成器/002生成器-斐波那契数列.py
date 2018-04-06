"""
生成器斐波那契数列：
"""

"""
In [3]: def createNum():
   ...:     print("---start---")
   ...:     a,b = 0,1
   ...:     for i in range(5):
   ...:         print("---1---")
   ...:         yield b           # yield:将函数变为生成器的标志，返回yield后面的值，并保存现场(状态),
   # 下次使用next(Generator Object)时，再从上次保存现场的位置继续执行；
   ...:         print("---2---")
   ...:         a,b = b,a+b
   ...:         print("---3---")
   ...:     print("---stop---")
   ...:     

In [4]: a = createNum()  # 已经不再是函数，里面的语句只有在通过next()调用的时候才会执行；

In [5]: a
Out[5]: <generator object createNum at 0x7f7b91cbc410>

In [6]: next(a)
---start---
---1---
Out[6]: 1    # yield返回值，并暂停，

In [7]: next(a)
---2---    # 从上次暂停的位置开始继续执行；
---3---
---1---
Out[7]: 1

In [8]: next(a)
---2---
---3---
---1---
Out[8]: 2

In [9]: next(a)
---2---
---3---
---1---
Out[9]: 3

In [10]: next(a)
---2---
---3---
---1---
Out[10]: 5

In [11]: next(a)   
---2---
---3---
---stop---
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-11-15841f3f11d4> in <module>()
----> 1 next(a)

StopIteration:   # 直到所有的对象都返回完了，你还要它继续生，它就会告诉你超生了；

"""


