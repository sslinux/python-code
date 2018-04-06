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

xiaotq = Xiaotq()
xiaotq.fly()

xiaotq.bark()  # 继承自父类Dog；

xiaotq.eat()   # 继承自父类的父类Animal；
# 继承可以是多重继承；








