# 命名空间：名称生效的范围；

def test():
    print("---test---")

"""
globals()    # 打印当前名称空间内的所有全局变量；
locals()     # 打印当前命名空间内的所有本地变量；
"""

# LEGB原则:
"""
locals --> enclosing function --> globals --> builtins
"""

# 查看内建变量:
dir(__builtins__)
