a = 100
b = a                 # 赋值：相当于将赋值运算符右侧的对象引用的内存地址，给了赋值运算符左侧的对象；

print(id(a),id(b))

# 任何使用赋值运算符的地方，都是引用；

# 查看一个对象的引用计数，可以使用sys.getrefcount(object)


