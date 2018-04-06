# 第一种: 引入第三个变量；
a = 4
b = 5
c = a
a = b
b = c
print("a=%d,b=%d"%(a,b))

# 第二种:  不引入第三个变量，任何语言都适用；
a = 4
b = 5
a = a + b
b = a - b
a = a - b
print("a=%d,b=%d"%(a,b))

# 第三种：  # python独有，不引入中间变量；
a = 4
b = 5
a,b = b,a 
print("a=%d,b=%d"%(a,b))