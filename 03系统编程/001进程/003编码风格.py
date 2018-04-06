
# pep8 编码规范

# 自行查看

"""
Python Enhancement Proposals ：python改进方案

https://www.python.org/dev/peps/
"""

# Guido的关键点之一是：代码更多是用来读而不是写。编码规范旨在改善Python代码的可读性。

# 风格指南强调一致性。项目、模块或函数保持一致都很重要。



# 每级缩进用4个空格。

# 括号中使用垂直隐式缩进或使用悬挂缩进。后者应该注意第一行要没有参数，后续行要有缩进。

"""
# 正确使用方式：

# 对准左括号
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 不对准左括号，但加多一层缩进，以和后面内容区别。
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 悬挂缩进必须加多一层缩进.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
"""