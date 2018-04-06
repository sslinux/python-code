"""
假设两个线程t1和t2都要对num=0进行增1运算，t1和t2都各对num修改10次，num的最终的结果应该为20。

但是由于是多线程访问，有可能出现下面情况：
    在num=0时，t1取得num=0。
    此时系统把t1调度为”sleeping”状态，把t2转换为”running”状态，t2也获得num=0。
    然后t2对得到的值进行加1并赋给num，使得num=1。
    然后系统又把t2调度为”sleeping”，把t1转为”running”。
    线程t1又把它之前得到的0加1后赋值给num。
    这样，明明t1和t2都完成了1次加1工作，但结果仍然是num=1。
"""

from threading import Thread
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1   # 该语句的两个操作可能会因为CPU时间片的轮转而导致数据不一致；

    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()

time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)


"""
问题产生的原因就是没有控制多个线程对同一资源的访问，对数据造成破坏，使得线程运行的结果不可预期。
这种现象称为“线程不安全”。
"""
