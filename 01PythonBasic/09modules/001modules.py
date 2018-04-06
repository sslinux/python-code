# In [1]: import os

# In [2]: os.__file__
# Out[2]: '/home/sslinux/.pyenv/versions/3.6.4/lib/python3.6/os.py'


import random 

from random import randint,randrange 

from random import *    # 尽量少用，容易造成名称空间冲突。

import time as tt   # 给time起别名为tt，只能用别名使用模块；


def test1():
    """DocString"""
    print("----test1----")

def test2():
    """DocString"""
    print("----test2----")

class ClassName(object):
    """docstring
     for ClassName"""

    def __init__(self,arg):
        pass 


def main():
    test1()
    test2()




print(__name__)
# __name__ 
# 被其他模块导入时，值为模块名；
# 自主执行的时，值为__main__

# 所以，习惯这样写：
if __name__ == "__main__":
    main()







