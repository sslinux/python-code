# class Tool(object):
#     def __init__(self,new_name):
#         self.name = new_name

# num = 0
# tool1 = Tool("铁撬")
# num+=1
# print(num)

# num = 0
# tool1 = Tool("工兵铲")
# num+=1
# print(num)

# num = 0
# tool1 = Tool("水桶")
# num+=1
# print(num)

class Tool(object):
    # 类属性:
    num = 0

    # 方法:
    def __init__(self,new_name):
        # 实例属性:
        self.name = new_name
        # 对类属性+1：
        Tool.num += 1
"""
实例属性：和具体的某个实例对象有关系，并且一个实例对象和另外一个实例对象是不共享属性的；
类属性： 类属性所属于类对象，并且多个实例对象之间共享一个类属性；
"""

tool1 = Tool("铁撬")
tool1 = Tool("工兵铲")
tool1 = Tool("水桶")
print(Tool.num)