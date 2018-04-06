"""
使用type()——元类，动态地创建类：
格式：
ClassName = type("ClassName",(BaseClass1,BaseClass2...),{'attr1':'value1','attr2':'value2'...})
"""

# 使用type()创建没有类属性的类：
"""
In [1]: class Test:
   ...:     pass 
   ...: 

In [2]: t1 = Test()

In [3]: Test2 = type("Test2",(),{})

In [4]: t2 = Test2()

In [5]: type(t1)
Out[5]: __main__.Test

In [6]: type(t2)
Out[6]: __main__.Test2
"""


# 使用type()创建有类属性的类：
"""
In [7]: class Person:
   ...:     nums = 0
   ...:     
In [12]: Person2 = type("Person2",(),{"nums":0})

In [13]: p1 = Person()

In [14]: p1.nums
Out[14]: 0

In [15]: p2 = Person2()

In [16]: p2.nums
Out[16]: 0
"""

# type()添加有实例方法的类：
"""
In [23]: def printNum(self):
    ...:     print("---num=%d---"%self.num)
    ...:     

In [24]: Test3 = type("Test3",(),{"printNum":printNum})

In [25]: t1 = Test3()

In [26]: t1.num = 100

In [27]: t1.printNum()
---num=100---

###############################等价于:#####################################

In [28]: class printNum2():
    ...:     def printNum(self):
    ...:         print("---num=%d---"%self.num)
    ...:         

In [29]: t2 = printNum2()

In [30]: t2.num = 100

In [31]: t2.printNum()
---num=100---
"""

# type() 创建有继承关系的类：
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

In [36]: Cat = type("Cat",(Animal,),{})   # type()中的类名需要使用引号，继承的类不需要引号，但只有一个基类时，元组中要用引号结尾；

In [37]: xiao_hua_mao = Cat()

In [38]: xiao_hua_mao.eat()
---eat---
"""