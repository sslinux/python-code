# 所谓多态：定义时的类型和运行时的类型不一样，此时就称为多态；

class Dog(object):
    def print_self(self):
        print("大家好，我是XXX，希望大家以后多多关照...")
    
class Xiaotq(Dog):
    def print_sef(self):
        print("Hello everybody,我是你们的老大，我是XXX")

def introduce(temp):     # 函数定义时，并不确定执行的是哪一个类中的print_self方法；
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)         #　只有当真正调用时才直到，执行的是哪个类中的print_self方法；

introduce(dog2)

# python是动态类型语言；
# 面向对象的三特性：封装、继承、多态；




