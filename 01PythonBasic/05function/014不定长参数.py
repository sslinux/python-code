# def sum_nums(a,b,*args):    # 可变长度位置参数；
#     print("-"*30)
#     print(a)
#     print(b)
#     print(args)

# sum_nums(11,22,33,44,55,66,77)
# sum_nums(11,22,33)
# sum_nums(11,22)


def sum_nums(a,b,*args):    # 可变长度位置参数；
    result = a+b
    for num in args:
        result += num 
    print("reuls=%d"%result)
    return result

sum_nums(11,22,33,44,55,66,77)
sum_nums(11,22,33)
sum_nums(11,22)