a = "lao"
b = "wang"
c = "zhao"

# 第一种方式：
d = a + b 

# 第二种方式：
e = "===" + a + b + "==="

# 第三种方式：
f = "===%s==="%(a+b)

# 第四种方式：
g = "==={s}===".format(s=a+b)


print(d) 
print(e)
print(f)
print(g)
