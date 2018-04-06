"""
类装饰器
"""

"""
In [5]: class Test():
   ...:     pass 
   ...: 

In [6]: t = Test()

In [7]: t()  # 正常情况下，实例对象t是不可调用的；
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-bf1592f10eb3> in <module>()
----> 1 t()

TypeError: 'Test' object is not callable

"""
#############################################################################
"""
In [2]: class Test(object):
   ...:     def __call__(self):
   ...:         print("---test---")
   ...:         

In [3]: t = Test()

In [4]: t()    # 类中实现了__call__()方法的实例对象是可以调用的；
---test---
"""

# 类的特殊方法回忆：
"""
__new__
__init__
__del__
__str__
__call__
"""

# 类装饰器：
"""
In [8]: class Test(object):
   ...:     def __init__(self,func):
   ...:         print("---初始化---")
   ...:         print("func name is %s"%func.__name__)
   ...:         self.__func = func
   ...:     def __call__(self):
   ...:         print("---装饰器中的功能---")
   ...:         self.__func()
   ...:         

In [9]: @Test   # test = Test(test),右边创建了一个实例对象，左边的test指向了这个实例对象，调用test()就会执行实例对象的__call__()方法；
   ...: def test():
   ...:     print("---test---")
   ...:     
---初始化---
func name is test

In [10]: test()
---装饰器中的功能---
---test---

"""