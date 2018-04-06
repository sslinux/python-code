class Cat:
    """定义了一个Cat类"""

    # 初始化对象:
    def __init__(self):       # 实例化对象时，__init__方法会被python解释器自动调用；
        print("---haha---")
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝kele...")
    def introduce(self):
        print("%s的年龄是%d"%(self.name,self.age))
        # self:替代实例的名字；相当于C++中的this.

# 创建一个对象：
tom = Cat()
tom.eat()
tom.drink()
tom.name = "汤姆"
tom.age = 40

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 15
lanmao.introduce()

#总结：实例化类的过程：
# 1、创建一个对象；
# 2、pyhon会自动调用__init__方法；
# 3、返回创建的对象引用给变量名；

