def createNum():
    print("---start---")
    a,b = 0,1
    for i in range(5):
        print("---1---")
        yield b
        print("---2---")
        a,b = b,a+b
        print("---3---")
    print("---stop---")

a = createNum()

# 以下两种方式是等价的：
ret = a.__next__()
print(ret)

print(next(a))





