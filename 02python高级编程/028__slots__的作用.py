"""
python在定义class的时候，使用__slots__变量，来限制class实例能添加的属性。
"""

"""
In [1]: class Person(object):
   ...:     __slots__ = ("name","age")
   ...:     

In [2]: P = Person()

In [3]: P.name = "laowang"

In [4]: P.age = 18

In [6]: P.gender = "Male"    # 添加额外的属性时，会报错；
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-85acfcaa450d> in <module>()
----> 1 P.gender = "Male"

AttributeError: 'Person' object has no attribute 'gender'

"""