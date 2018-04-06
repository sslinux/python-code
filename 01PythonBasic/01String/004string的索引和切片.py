name = 'abcde'

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# IndexError 索引错误，越界；

# 字符串从右往左取元素，可以使用-1,-2
name[len(name)-1]  == name[-1]

# 切片：
name = 'abcdefABCDEF'
print(name[2:5])  # 不包含下标为5的元素；左闭右开区间；

print(name[2:-1])
print(name[2:])   # 后面不写的话，默认取到最后一个；

print(name[2:-1:2])  # 格式：[start:stop:step] step默认为1；

# 逆序，倒序：
print(name[-1::-1])  # 从-1开始，stop位置省略，step为-1
print(name[::-1])    # 上一行的简写；


