class Dog(object):
    
    # 私有类属性：
    __instance = None 

    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self,name):
        self.name = name 

# 现在的这个单例对象是可以初始化(__init__)多次的:                      
a = Dog("旺财")
print(id(a))
print(a.name)
b = Dog("啸天犬")
print(id(b))
print(b.name)