class Cat:
    """定义了一个Cat类"""

    # 初始化对象:
    def __init__(self,new_name,new_age):       # 实例化对象时，__init__方法会被python解释器自动调用；
        self.name = new_name
        self.age = new_age
    def __str__(self):     # 魔法方法，这个方法返回的信息，就是您直接打印实例化对象时的内容；
        return "%s的年龄是:%d"%(self.name,self.age)

    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝kele...")
    def introduce(self):
        print("%s的年龄是%d"%(self.name,self.age))

tom = Cat("汤姆",40)
lanmao = Cat("蓝猫",10)

print(tom)
print(lanmao)