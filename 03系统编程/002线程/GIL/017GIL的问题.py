"""
GIL: 全局解释器锁

"""


"""
# 单线程死循环，占满CPU

while True:
    pass

# 空跑，车停着踩油门
"""



# 两个线程的死循环：不会占满多核CPU

"""
import threading

# 子进程死循环：
def test():
    while True:
        pass

t1 = threading.Thread(target=test)
t1.start()

# 主进程死循环：
while True:
    pass
"""

# 在多线程中，其实是假的多线程；
"""
    GIL保证了同一时刻，多个线程中，只有一个被调用；
    在实现多任务时，多线程的效率没有多进程的高；多核的时候更明显；
"""

# 连个进程的死循环：会占满多核CPU；
"""
import multiprocessing

def deadLoop():
    while True:
        pass

# 子进程死循环：
p1 = multiprocessing.Process(target=deadLoop)
p1.start()

# 主进程死循环:
deadLoop()
"""


# 克服GIL导致的问题：
"""
1、能用进程的尽量用进程；
2、多线程时，使用C语言编写target指向的函数；
"""
