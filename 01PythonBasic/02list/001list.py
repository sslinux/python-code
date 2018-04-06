# 列表

names = ['老王','老李','老刘']   # 定义了一个列表；

# C语言中的数组 int nums[]{11,22,33,44,55}

nums = [11,22,3.14,'100',"laowang"]

# 增删改查：

# 添加新的元素：
names.append("老赵")   # 追加在列表最后；
# names.insert(index,ITER)
names.insert(0,"八戒")
names.extend(nums)   # 等价于 names + nums

# 删：
names.pop()      # 删除最后一个元素，并返回该元素；
names.remove('老王')   # 删除列表中的第一个'老王‘元素；
del names[2]         # 删除指定索引的元素；

# 列表的切片操作，返回新的列表；

# 改：
names[0] = "猪八戒"  

# 查
# 1、成员判断： in或not in



