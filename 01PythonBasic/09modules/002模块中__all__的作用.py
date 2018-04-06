__all__ = ["test1","test2","num","Test"]   
# 在别的模块中导入该模块，使用from ModuleName import *时：
# 只会导入__all__变量中的对象——使用字符串形式定义；

def test1():
    print("---test-1---")

def test2():
    print("---test-2---")

num = 0

class Test(object):
    pass 



# 总结：
# __all__ = ['a','b,']
# 上述用法用在模块中时，表示使用(from ModuleName import *)时导入那些对象；
# 如果是用在包的__init__.py文件中时，表示使用(from PackageName import *)时导入哪些模块文件；

