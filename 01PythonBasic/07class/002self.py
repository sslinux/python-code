class Cat:
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝kele...")
    def introduce(self):
        print("%s的年龄是%d"%(self.name,self.age))
        # self:替代实例的名字；相当于C++中的this.

tom = Cat()
tom.eat()
tom.drink()

# 给tom对象添加属性:
tom.name = "汤姆"
tom.age = 40

# 获取属性的第一种方式:
print("%s的年龄是%d"%(tom.name,tom.age))

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 15

lanmao.introduce()