"""
动态添加实例方法：
"""

class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("---%s正在吃---"%self.name)

def run(self):
    print("---%s正在跑---"%self.name)

p1 = Person("老王",10000)
p1.eat()

import types   

p1.run = types.MethodType(run,p1)  # 将run函数绑定到实例对象p1，并将p1对象作为第一个参数传递；

p1.run() 