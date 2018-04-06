"""
线程的执行顺序不确定，由操作系统自行调度；
"""

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)
            print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == "__main__":
    test()


# 线程的执行顺序 和 线程的创造顺序无关。

"""
多线程程序的执行顺序是不确定的。当执行到sleep语句时，线程将被阻塞（Blocked），到sleep结束后，线程进入就绪（Runnable）状态，等待调度。
而线程调度将自行选择一个线程执行。上面的代码中只能保证每个线程都运行完整个run函数，但是线程的启动顺序、run函数中每次循环的执行顺序都不能确定。
"""

"""
总结:
    1、每个线程一定会有一个名字，尽管上面的例子中没有指定线程对象的name，但是python会自动为线程指定一个名字。
    2、当线程的run()方法结束时该线程完成。
    3、无法控制线程调度程序，但可以通过别的方式来影响线程调度的方式。
    4、线程的几种状态：
        新建--启动-->就绪<--调度-->运行--结束-->死亡
                    等待(堵塞)
"""
