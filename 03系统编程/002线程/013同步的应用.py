"""
2. 什么是同步
    同步就是协同步调，按预定的先后次序进行运行。如:你说完，我再说。
    "同"字从字面上容易理解为一起动作
    其实不是，"同"字应是指协同、协助、互相配合。
    如进程、线程同步，可理解为进程或线程A和B一块配合，A执行到一定程度时要依靠B的某个结果，于是停下来，示意B运行;B依言执行，再将结果给A;A再继续操作。

3. 解决问题的思路：
    对于本小节提出的那个计算错误的问题，可以通过线程同步来进行解决

    思路，如下:
        系统调用t1，然后获取到num的值为0，此时上一把锁，即不允许其他现在操作num
        对num的值进行+1
        解锁，此时num的值为1，其他的线程就可以使用num了，而且是num的值不是0而是1
        同理其他线程在对num进行修改时，都要先上锁，处理完后再解锁，在上锁的整个过程中不允许其他线程访问，就保证了数据的正确性
"""

"""
堵塞-非堵塞
同步-异步
"""

# 多个线程有序执行：

from threading import Thread,Lock
from time import sleep

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("------Task 1 -----")
                sleep(0.5)
                lock2.release()

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("------Task 2 -----")
                sleep(0.5)
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("------Task 3 -----")
                sleep(0.5)
                lock1.release()

#使用Lock创建出的锁默认没有“锁上”
lock1 = Lock()
#创建另外一把锁，并且“锁上”
lock2 = Lock()
lock2.acquire()
#创建另外一把锁，并且“锁上”
lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()

# 可以使用互斥锁完成多个任务，有序的进行工作，这就是线程的同步
