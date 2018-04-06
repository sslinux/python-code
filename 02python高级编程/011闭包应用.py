# def test(a,b):

#     def test_in(x):
#         print(a*x+b)

#     return test_in 

# line1 = test(1,1)
# line1(0)

# line2 = test(10,4)
# line2(0)

# line1(0)


#########################################
def createNum(a,b,x):
    print(a*x+b)

createNum(1,3,5) 
createNum(1,3,6)   # 本只需要改变x的值，a、b的值不变，但是每次都需要传递三个参数；


def test(a,b):
    def test_in(x):
        print(a*x+b)
    return test_in 

line1 = test(1,1)
line1(0)
line1(2)   # a,b的值不变，只需要传入新的x的值；

line2 = test(10,4)
line2(0)
line2(3)   # a,b的值不变，只需要传入新的x的值；

line1(0)   # 当a=1,b=1时创建的对象，依然还保存着；可以直接使用；

