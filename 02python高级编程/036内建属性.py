"""
经典类(旧式类),早期如果没有要继承的父类,继承里空着不写的类.

#py2中无继承父类，称之经典类,py3中已默认继承object
class Person:
    pass

查看某个对象的内建属性：dir(object)

子类没有实现__init__方法时，默认自动调用父类的。 如果自己定义__init__方法时，需自己手动调用父类的 __init__方法。
"""

# 常用专有属性       说明                    触发方式
"""
__init___           构造初始化函数           创建实例后，赋值时使用，在__new__后；
__new__             生成实例所需属性          创建实例时
__class__           实例所在的类              实例.__class__
__str__             实例字符串表示，可读性      print(类实例),如果没有实现，使用repr结果
__repr__            实例字符串表示，准确性      类实例 回车 或者 print(repr(类实例))
__del__             析构                     del删除实例
__dict__            实例自定义属性             vars(实例.__dict__)
__doc__             类文档，子类不继承          help(类或实例)
__getattribute__    属性访问拦截器             访问实例属性时
__bases__           类的所有父类构成元素        类名.__bases__
"""

# __str__() 和 __repr__()的区别：
"""
In [23]: a = "hello world"

In [24]: a
Out[24]: 'hello world'

In [25]: print(a)
hello world

In [27]: a.__str__()
Out[27]: 'hello world'

In [28]: a.__repr__()
Out[28]: "'hello world'"
"""

# __getattribute__() 属性访问拦截器；
# 获取属性时，必须先调用该方法，该方法的返回值就是属性的值；

# __getattribute__()    ===>> 属性访问拦截器1:
"""
class Human(object):
    def __init__(self,name,age=18,gender="Female"):
        self.name = name
        self.age = age
        self.gender = gender

    def __getattribute__(self,attr):
        if attr == "age":
            print("女人的年龄是秘密，不要随便乱问！")
            return "Secret"
        else:
            return object.__getattribute__(self,attr)      

    
sherry = Human("Sherry")
print(sherry.name)
print(sherry.gender)
print(sherry.age)
"""

# __getattribute__()    ===>> 属性访问拦截器2:

"""
class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    #属性访问时拦截器，打log
    def __getattribute__(self,obj):   # 重写了__getattribute__()方法时，obj = "subject1"
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:   #测试时注释掉这2行，将找不到subject2
            return object.__getattribute__(self,obj)     # 建议这种写法，不想拦截的属性(默认情况)调用父类的__getattribute__()方法正常返回。

    def show(self):
        print('this is Itcast')

s = Itcast("python")
print(s.subject1)
print(s.subject2)
"""

# __getattribute__()    ===>> 属性访问拦截器3:拦截方法(方法也是属性之一)

class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    # 属性访问拦截器，打log
    def __getattribute__(self,obj):
        print("===1>%s"%obj)
        if obj == "subject1":
            print("log subject1")
            return 'redirect python'
        else:
            temp = object.__getattribute__(self,obj)
            print("===>2%s"%str(temp))
            return temp

    def show(self):
        print('this is Itcast')

s = Itcast("python")
print(s.subject1)
print(s.subject2)

s.show()    
# 调用方法时分两步：
# 1、先获取show属性对应的结果，应该是一个方法；
# 2、用返回的函数名加小括号进行调用；


# 对象的方法也只是一个属性，但这个属性指向的是一个函数，并且传递对象自身作为第一个参数而已。

"""
In [29]: class Test:
    ...:     pass 
    ...: 

In [30]: t = Test()

In [31]: t.num
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-31-4c0ffbc8a4be> in <module>()
----> 1 t.num

AttributeError: 'Test' object has no attribute 'num'

In [32]: t.getNum()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-32-2eac24aaf540> in <module>()
----> 1 t.getNum()

AttributeError: 'Test' object has no attribute 'getNum'
"""


# __getattribute__()的坑：

class Person(object):
    def __getattribute__(self,obj):
        print("---test---")
        if obj.startswith("a"):
            return "hahha"
        else:
            return self.test    # 主要坑在这里，self.test会调用__getattribute__()，造成死循环；
            # 希望此处使用之前建议的写法，用父类的__getattribute__()方法获得值；
            # return object.__getattribute__(self,obj)


    def test(self):
        print("heihei")


t = Person()

t.a #返回hahha

t.b #会让程序死掉
    #原因是：当t.b执行时，会调用Person类中定义的__getattribute__方法，但是在这个方法的执行过程中
    #if条件不满足，所以 程序执行else里面的代码，即return self.test  问题就在这，因为return 需要把
    #self.test的值返回，那么首先要获取self.test的值，因为self此时就是t这个对象，所以self.test就是
    #t.test 此时要获取t这个对象的test属性，那么就会跳转到__getattribute__方法去执行，即此时产
    #生了递归调用，由于这个递归过程中 没有判断什么时候推出，所以这个程序会永无休止的运行下去，又因为
    #每次调用函数，就需要保存一些数据，那么随着调用的次数越来越多，最终内存吃光，所以程序 崩溃
    #
    # 注意：以后不要在__getattribute__方法中调用self.xxxx



