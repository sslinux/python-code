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

for num in a:      # 使用for循环去遍历生成器的时候，不会越界，所以不会产生StopIteration的异常；
    print(num)        

