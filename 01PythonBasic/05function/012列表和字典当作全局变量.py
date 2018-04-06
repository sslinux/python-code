nums = [11,22,33]
info = {'name':'laowang'}

def test():
    """
    修改全局变量(列表和字典)的值:
    当列表和字典作为全局变量时，在函数中使用时可以不使用关键字global声明，
    当为了提高代码的可读性，建议使用关键字global写明；    
    """
    nums.append(44)
    info['age'] = 18

def test2():
    print(nums)
    print(info)

test()
test2()