# 动态：在运行时可以改变其结构；

# a = 100
# def test():
#     print("---test---")

# a = test
# a() 

# class Test(object):
#     pass 

# t = Test()   

# dir(t)     

# t.age = 18    # 定义时并没有属性age，现在是动态添加；

class Person(object):
    def __init__(self,new_name,new_age):
        self.name = new_name     
        self.age = new_age 


laowang = Person("laowang",18) 
print(laowang.name)
print(laowang.age)

# print(laowang.addr)    # 并没有这个属性；

laowang.addr = "北京"   # 添加的是实例对象的属性；
print(laowang.addr)  

laozhao = Person("laozhao",18)
# print(laozhao.addr)   # laozhao并没有属性addr

# 添加类属性:
Person.num = 100
print(laowang.num) 
print(laozhao.num)