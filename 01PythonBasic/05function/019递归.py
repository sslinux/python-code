# 求阶乘：

'''
i = 1 
result = 1
while i<=4:
    result = result * i
    i += 1
print(result)
'''


# 5! => 5*4!
# 4! => 4*3!

def getNums(num):
    if num > 1:
        return num * getNums(num-1) 
    else:
        return num

result = getNums(4)
print(result)

# 总结：递归是函数嵌套调用的特殊情况，调用的是函数自己；

# 使用递归，一定要有结束递归的条件，否则会耗尽内存导致程序结束；




