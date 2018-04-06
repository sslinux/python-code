class Dog(object):
    def __init__(self):
        print("---init方法---")

    def __del__(self):
        print("---del方法---")

    def __str__(self):
        print("---str方法---")
        return "对象的描述信息"

   # 定义类时，真正创建实例对象的方法是__new__()，如果你在定义类时重写了这个方法而不知道如何创建对象的话，需要调用父类的__new__(cls)方法完成创建实例的工作； 
    def __new__(cls):   # cls此时是Dog指向的那个类对象；
        print(id(cls))
        print("---new方法---") 
        return object.__new__(cls)

print(id(Dog))

xtq = Dog()
# 实例化过程：相当于要做3件事情：
# 1、调用__new__方法来创建对象，然后找了一个变量来接收__new__的返回值，这个返回值表示创建出来的对象的引用；
# 2、__init__(刚刚创建爱呢出来的对象的引用)
# 3、返回对象的引用；

# __new__和__init__的组合使用就是其他语言中的构造方法；
