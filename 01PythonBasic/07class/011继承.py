# 父类，基类

# 子类，派生类 


class Animal:
    def eat(self):
        print("----吃----")
    def drink(self):
        print("----喝----")
    def sleep(self):
        print("----睡----")
    def run(self):
        print("----跑----")

class Dog(Animal):
    """
    def eat(self):
        print("----吃----")
    def drink(self):
        print("----喝----")
    def sleep(self):
        print("----睡----")
    def run(self):
        print("----跑----")
    """
    def bark(self):
        print("----汪汪叫----")

class Cat(Animal):
    def catch(self):
        print("----抓老鼠----")

# a = Animal()
# a.eat()

wangcai = Dog()    # wangcai只能使用Dog、Animal类中的方法；
wangcai.eat()

tom = Cat()        # tom只能使用Cat、Animal类中的方法； 
tom.eat()

