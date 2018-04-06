myStr = "hello world itcast adn itcastxxxcpp"

myStr.find("world")   # 返回第一次找到的字符串的索引；  返回-1表示未找到；
myStr.rfind('itcast') # 从右往左找；

myStr.index("world") # 返回索引，但未找到会返回ValueError；
myStr.rindex("world") # 从右往左找；


myStr.count('world')   # 统计出现的次数；

myStr.replace("world","WORLD")   # 无法修改原字符串，生成新的字符串；
myStr.replace("itcast","ITCAST",1)  # 1表示替换的次数；

myStr.split(" ")  # 返回列表，按空格切割为列表中的元素；

myStr.capitalize()  # 首单词首字母大写；
myStr.title()  # 所有单词的首字母大写；

myStr.startswith("he")   # 判断是否以指定字符串开头；
myStr.endswith('cpp')    # 判断是否以指定字符串结尾；

myStr.lower()   # 转换为小写；
myStr.upper()   # 转换为大写；


myStr.ljust(50)   # 靠左对齐，50表示总共用多少宽度；
myStr.rjust(50)   # 靠右对齐
myStr.center(50)  # 居中对齐

myStr.lstrip()    # 去除左边的空格；
myStr.rstrip()    # 去除右边的空格；
myStr.strip()     # 去除左右两边的空格；

myStr.partition('itcast')  # 返回元组，以指定字符串为分隔，将字符串分隔为三部分(前，指定字符串，后)
myStr.rpartition('itcast')         # 从右往左找；

myStr.splitlines()         # 以换行符进行切割，返回列表；

myStr.isalpha()   # 判断是否是纯字母；
myStr.isdigit()   # 是否是纯数字；
myStr.isalnum()   # 是否是字母和数字；

# " ".join()   # 连接元素；

