"""
为了让每个线程的封装性更完美，所以使用threading模块时，
往往会定义一个新的子类class，只要继承threading.Thread就可以了，然后重写run方法
"""

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i) # name属性中保存的是当前线程的名字；
            print(msg)

if __name__ == "__main__":
    t = MyThread()
    t.start()

#
# python的threading.Thread类有一个run方法，用于定义线程的功能函数，可以在自己的线程类中覆盖该方法。
#
# 而创建自己的线程实例后，通过Thread类的start方法，可以启动该线程，交给python虚拟机进行调度，当该线程获得执行的机会时，就会调用run方法执行线程。

"""
僵尸进程:如果一个进程结束了，父进程没有回收它的资源；
孤儿进程:父进程挂了，子进程还没有，这是的子进程就是孤儿进程；pid为1的进程(init)是孤儿收容院；
所以，父进程要等待子进程结束后才会结束；
"""
