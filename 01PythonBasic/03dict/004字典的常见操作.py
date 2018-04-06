info = {"name":"laowang","age":18,"addr":"sichuan"}


print(len(info))    # 打印字典中的元素个数；

print(info.keys())  # info.keys()，py2中返回一个包含字典中所有键的列表，py3中返回的是一个可迭代对象；
print(info.values())  # info.values(),py2中返回一个包含字典中所有值的列表,py3中返回的是一个可迭代对象；
print(info.items())   # info.items(),返回形如：(key:value)的元组，组成的列表；

for temp in info.items():
    print(temp)


for temp in info.items():
    print("key=%s,value=%s" % (temp[0],temp[1]))

for A,B in info.items():
    print("key=%s,value=%s"%(A,B))

