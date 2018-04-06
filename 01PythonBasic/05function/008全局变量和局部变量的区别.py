# def get_wendu():
#     wendu = 33
#     return wendu 

# def print_wendu(wendu):
#     print("温度是%d"%wendu)



# wendu = get_wendu() # 若函数有返回值，则需要有一个变量来接收；
# print_wendu(wendu)

# 定义全局变量：
wendu = 0  # global;

def get_wendu():
    # wendu = 33  # 此处是局部变量；   
    # return wendu 

    # 在函数中若想修改全局变量，需要使用关键字global，但不建议这样使用；
    global wendu
    wendu = 33

def print_wendu():
    print("温度是%d"%wendu)

get_wendu()
print_wendu()