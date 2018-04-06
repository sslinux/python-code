# class Test(object):
#     def __init__(self):
#         self.__num = 100 

#     def setNum(self,new_num):
#         self.__num = new_num

#     def getNum(self):
#         return self.__num 

# t = Test()
# t.setNum(50)
# print(t.getNum())


# **********************************************************

class Test(object):
    def __init__(self):
        self.__num = 100 

    def setNum(self,new_num):
        self.__num = new_num

    def getNum(self):
        return self.__num 

    num = property(getNum,setNum)   # 使用property；
# 基于此种方式，可以将类中需要与外界交互的属性通过方法的方式去改变它的值，以便于判断改变时是否合法(在方法中加判断)；

t = Test()
t.num = 200  # 相当于调用了 t.setNum(200)
print(t.num) # 相当于调用了 t.getNum()

"""
注意点：
t.num 到底是调用getNum()还是setNum()，要根据实际的场景来判断：
1、如果是给t.num赋值，那么就一定调用setNum()
2、如果是获取t.num的值，那么就一定调用getNum()
property的作用：相当于把方法进行了封装，开发者在对属性设置数据的时候更方便；
"""