from threading import Thread,Lock
import time

g_num = 0

def test1():
    global g_num

    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        mutex.acquire()     # 多进程争用资源的时候需要上锁； # 上锁的范围越小越好；
        g_num += 1
        mutex.release()
    print("---test2---g_num=%d"%g_num)

# 创建一把互斥锁，这个锁默认是没有上锁的：
mutex = Lock()

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)


"""
等待解锁的方式：
    通知： 一方解锁时，通知其它抢着上锁的线程；
    轮询： 浪费资源；
"""
