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
    def bark(self):
        print("----汪汪叫----")

class Xiaotq(Dog):
    def fly(self):
        print("----飞----")
    def bark(self):               # 重写方法，和父类中的方法同名； 用子类中的同名方法覆盖父类中的方法；
        print("----狂叫---")

        # 第1种调用被重写的父类的方法：
        # Dog.bark(self)    # 调用Dog类中的bark()方法，必须传递参数(self).

        # 第2种：
        super().bark()    # 调用父类中的bark()

xiaotq = Xiaotq()
xiaotq.fly()

xiaotq.bark()

xiaotq.eat()     