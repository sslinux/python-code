# import导入模块 

# import的搜索路径：
import sys
print(sys.path)

# sys.path 是一个列表，每个元素是一个路径，从前往后搜索；第一次搜索到后将不再继续往后搜索；

sys.path.append("/home/sslinux/python/lib")

'''
#include "xxx.h"
#include "../hello.h"
'''


# 模块被导入后，模块被修改，程序不能重新导入模块的新功能;

# 可以使用以下方式，重新加载模块：
from imp import * 
reload(ModuleName)



