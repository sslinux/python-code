
"""
非全局变量不需要上锁
"""
import threading
from threading import Thread
import time

def test1():
    name = threading.current_thread().name
    print("---thread name is %s ---"%name)
    g_num = 100
    if name == "Thread-1":
        g_num += 1
    else:
        time.sleep(2)

    print("---thread is %s---g_num=%d"%(name,g_num))

# def test2():
#     time.sleep(1)
#     g_num = 100
#     print("---test2---g_num=%d"%g_num)

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test1)
p2.start()

"""
在多线程开发中，全局变量是多个线程都共享的数据；
而局部变量等是各自线程的，是非共享的
"""
