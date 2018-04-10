# coding:utf-8

# 列表:
# li = []
# li.append()
# li.insert()

# timeit模块:
"""
class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
    Timer是测量小段代码执行速度的类。
    stmt参数是要测试的代码语句（statment）；
    setup参数是运行代码时需要的设置；
    timer参数是一个定时器函数，与平台有关。
"""

"""
timeit.Timer.timeit(number=1000000)
    Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。
    方法返回执行代码的平均耗时，一个float类型的秒数。
"""

from timeit import Timer

"""
li1 = [1, 2]
li2 = [23, 5]

li = li1 + li2

li = [i for i in range(10000)]

li = list(range(10000))

li = []
for i in range(10000):
    li.append(i)
"""

def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li = li + [i]
        # li += [i]  # += 经过优化，是在原有list上操作；类似于extend；

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

def test5():
    li = []
    for i in range(10000):
        li.extend([i])


timer1 = Timer("test1()","from __main__ import test1")
print("append:",timer1.timeit(1000))

timer2 = Timer("test2()","from __main__ import test2")
print("+:",timer2.timeit(1000))

timer3 = Timer("test3()","from __main__ import test3")
print("[i for i in range]:",timer3.timeit(1000))

timer4 = Timer("test4()","from __main__ import test4")
print("list(range()):",timer4.timeit(1000))

timer5 = Timer("test5()","from __main__ import test5")
print("extend:",timer5.timeit(1000))

print("*"*20)

def test6():
    li = []
    for i in range(10000):
        li.append(i)

def test7():
    li = []
    for i in range(10000):
        li.insert(0,i)

timer6 = Timer("test6()","from __main__ import test6")
print("append:",timer6.timeit(1000))

timer7 = Timer("test7()","from __main__ import test7")
print("insert(0):",timer7.timeit(1000))

# 运行结果：
"""
append: 0.5712949299995671
+: 0.5902853480001795
[i for i in range]: 0.21750077999968198
list(range()): 0.12271732299996074
extend: 0.9155622410016804
********************
append: 0.5574492750001809
insert(0): 12.13671424200038
"""
# append的效率高于insert



# pop第一个元素和pop最后一个元素的效率比较：
x = list(range(2000000))
pop_zero = Timer("x.pop(0)","from __main__ import x")
print("pop_zero ",pop_zero.timeit(number=1000), "seconds")

x = list(range(2000000))
pop_end = Timer("x.pop()","from __main__ import x")
print("pop_end ",pop_end.timeit(number=1000), "seconds")

# 运行结果：
# pop_zero  2.213147118998677 seconds
# pop_end  6.903799840074498e-05 seconds

