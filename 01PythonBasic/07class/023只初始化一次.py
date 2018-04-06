class Dog(object):
    
    # 私有类属性：
    __instance = None 
    __init_flag = False 

    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self,name):
        if Dog.__init_flag == False:
            self.name = name 
            Dog.__init_flag = True 

# 现在的这个单例对象只会初始化(__init__)一次了:                      
a = Dog("旺财")
print(id(a))
print(a.name)

b = Dog("啸天犬")
print(id(b))
print(b.name)   # 这里显示的还是'旺财'

