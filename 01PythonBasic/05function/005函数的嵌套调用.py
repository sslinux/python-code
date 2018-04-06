# def test1():
#     pass

# def test2():
#     print("-----2-1-----")
#     print("heihei")
#     print("-----2-2-----")

# def test3():
#     print("-----3-1-----")
#     test2()
#     print("-----3-2-----")

# test3()


# 函数的嵌套调用应用：

# def print_line():
#     print("-"*50)

# def print_5_line():
#     i = 0
#     while i < 5:
#         print_line()
#         i += 1

# print_5_line()

# 计算任意三个数的平均值；


def sum_3_nums(a,b,c):
    result = a+b+c
    # print("%d+%d+%d=%d"%(a,b,c,result))
    return result 

def average_3_nums(a1,a2,a3):
    result = sum_3_nums(a1,a2,a3)
    result /= 3
    print("平均值是:%d"%result)

#1、获取三个数值：
num1 = int(input("第1个值:"))
num2 = int(input("第2个值:"))
num3 = int(input("第3个值:"))

sum_3_nums(num1,num2,num3)
average_3_nums(num1,num2,num3)
