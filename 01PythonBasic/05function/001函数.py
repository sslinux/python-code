# 把具有独立功能的代码块，当作一个整体，是代码重复利用的最小单位，就是函数；

def print_menu():
    print("="*50)
    print(" 名片管理系统 v0.1")
    print(" 1:xxx")
    print(" 2:xxx")
    print("="*50)

# print_menu()


# 定义有参数的函数：
def sum_2_nums(a,b):
    result = a+b
    print("%d+%d=%d"%(a,b,result))

# 调用函数：
num1 = int(input("number1:"))
num2 = int(input("number2:"))
sum_2_nums(num1,num2)