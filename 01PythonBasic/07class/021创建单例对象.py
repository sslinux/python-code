
# class Dog(object):
#     pass 

# a = Dog()
# print(id(a))
# b = Dog()
# print(id(b))

# 单例：不管实例化多少次，返回的都是同一个对象的引用；

class Dog(object):
    
    # 私有类属性：
    __instance = None 

    def __new__(cls):
        # if xxx:
        #     return object.__new__(cls)
        # else:
        #     return 上一次创建的对象的引用
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
                       
a = Dog()
print(id(a))
b = Dog()
print(id(b))
