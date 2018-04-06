class Test(object):
    def __init__(self):
        self.__num = 100 

    def setNum(self,new_num):
        self.__num = new_num

    def getNum(self):
        return self.__num 

t = Test()
# print(t.__num)  # 直接取，是会报错的；
# t.__num = 200   # 此处相当于给实例新添加了一个属性；
# print(t.__num)  # 因为上一行添加了新的属性，这行不会报错；


"""
xx:公有变量
_x:单前置下划线，私有化属性或方法，from somemodule import * -->禁止导入，类对象和子类可以访问；
__xx:双前置下划线，避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
# 通过from MoudleName import * 的方式导入，访问不了;
# 但通过 import ModuleName的方式导入，可以访问。
__xx__:双前后下划线，用户名字空间的魔法对象或属性。例如__init__,__不要自己发明这样的名字；
xx_:单后置下划线，用于避免与Python关键词的冲突；
"""

# 通过name mangling(名字重整(目的就是以防子类意外重写基类的方法或者属性)如：_Class__object)机制就可以访问private了。

# 因为名字重整，所以私有变量其实是可以访问的： 重整后的名字是: _ClassName__Attr    # 但不建议使用；

