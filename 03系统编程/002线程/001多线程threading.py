"""
python的thread模块时比较底层的模块，
python的threading模块是对thread做了一些包装的，可以更加方便的被使用；
"""

# 1、使用threading模块：

# 1.1 单线程执行：
"""
import time

def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        saySorry()
"""

# 1.2 多线程执行：

import threading
import time

def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()  # 启动线程，即让线程开始执行；

# 说明:
    # 可以明显看出使用了多线程并发的操作，花费时间要短很多
    # 创建好的线程，需要调用start()方法来启动


from threading import Thread
import time

# 1、如果多个线程执行的都是同一个函数的话，各自之间不会有影响，各是各的；
def test():
    print("---昨晚喝多了，下次少喝点---")
    time.sleep(1)

for i in range(5):
    t = Thread(target=test)
    t.start()
