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

p1 = Person("p1",10)
p1.eat()

# p1.run = run 
# p1.run()  # 虽然p1对象中，run属性已经指向了run()函数，但是这句代码还不正确，
          # 因为run属性指向的函数，是后来添加的，即p1.run()的时候，并没有把p1当做第一个参数，导致了调用p1.run()的时候，出现了缺少参数的问题；

# 正确的方法应该是：
import types   
p1.run = types.MethodType(run,p1)

"""
 |  method(function, instance)
 |  
 |  Create a bound instance method object.
"""

p1.run()

