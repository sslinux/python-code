"""
动态添加静态方法：
"""

class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("---%s正在吃---"%self.name)

@staticmethod
def test():
    print("---static method---")

p1 = Person("老王",10000)
p1.eat()

Person.test = test    # 将静态方法绑定到P.test    
Person.test()    
