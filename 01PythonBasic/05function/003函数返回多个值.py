def test():
    a = 11
    b = 22
    c = 33
    # return a

    # 第一种方式：
    # d = [a,b,c]
    # return d 
    
    # 第二种：
    # return [a,b,c]

    # 第三种：
    # return (a,b,c)
    return a,b,c


num = test()
print(type(num))
print(num)