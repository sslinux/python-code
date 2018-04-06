# 将数据与函数绑定到一起，进行封装，这样能够更快速的开发程序，减少了重复代码的重写过程；

# 面向对象(object-oriented)
# 面向对象编程(Object Oriented Program)

# 类和对象：
# 类：抽象
# 对象：具体 

# 类的组成：
# 类名、属性、方法 


# 类名：human
# 属性：肤色、年龄、身高
# 方法：跑步、吃饭、睡觉、搞对象


# 定义一个类：
# class ClassName:
#     # 属性
#     # 方法
#     def xxx():
#         pass 

# class Cat:
#     # 属性

#     # 方法：
#     def eat(self):
#         print("猫在吃鱼...")
#     def drink(self):
#         print("猫正在喝kele...")

# # 创建一个对象：实例化
# tom = Cat()

# # 调用对象的方法：
# tom.eat()
# tom.drink()



# 定义类的属性：
class Cat:
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝kele...")
    def introduce(self):
        print("%s的年龄是%d"%(tom.name,tom.age))

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



