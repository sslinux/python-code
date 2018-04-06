"""
元类就是用来创建类(对象)的，元类就是类的类。

# 简单理解：
MyClass = MetaClass()   # 使用元类创建出一个对象，这个对象称为“类”
MyObject = MyClass()    # 使用“类”来创建出实例对象；
"""

# 验证type元类：
"""
In [32]: class Animal:
    ...:     def eat(self):
    ...:         print("---eat---")
    ...:         

In [33]: class Dog(Animal):
    ...:     pass
    ...: 

In [34]: wangcai = Dog()

In [35]: wangcai.eat()
---eat---

In [36]: Cat = type("Cat",(Animal,),{})

In [37]: xiao_hua_mao = Cat()

In [38]: xiao_hua_mao.eat()
---eat---

In [39]: Cat.__class__
Out[39]: type

In [40]: wangcai.__class__
Out[40]: __main__.Dog

In [41]: xiao_hua_mao.__class__
Out[41]: __main__.Cat

In [42]: Dog.__class__
Out[42]: type

In [43]: type.__class__   # type自己创造了自己；
Out[43]: type
"""


# 定义类时,若要指定自己的元类：

# python2:
"""
class ClassName:
    __metaclass__ = METACLASS 
    pass 
    #__metaclass__属性指定，由哪一个类来创造你定义的类；
"""

# python3:
"""
class ClassName(BaseClass,metaclass=METACLASS):
    pass 
"""
# 说明：
# METACLASS是变量，是自己定义的创造类的方法；
# 详细见：034和035


