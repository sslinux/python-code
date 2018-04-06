a = [11,22,33]
b = [44,55]

# a.extend(b)
# print(a)
# [11, 22, 33, 44, 55]


a.append(b)
print(a)
# [11, 22, 33, [44, 55]]


# append的注意点:
a = a.append(b)   # 是将a.append(b)的返回值 赋值给 a，而该返回值为None;

# 因为列表是可变对象，所以要查询a修改以后的值，因该是：
a.append(b)
print(a)
