
num = 10
print(id(num))
num = 20
print(id(num))

string = "hello"
print(id(string))
string = "world"
print(id(string))

t = (11,22,33)

# 在python中：
# 数字、字符串、元组是不可变类型； 只有不可变类型，才能作为字典的key;
# 列表和字典是可变类型； 列表和字典 不能作为字典的key；