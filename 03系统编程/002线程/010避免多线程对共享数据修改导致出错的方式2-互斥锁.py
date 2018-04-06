"""
当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制
线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。
互斥锁为资源引入一个状态：锁定/非锁定。
某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；
直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。
互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
"""


"""
threading模块中定义了Lock类，可以方便的处理锁定：
    # 创建锁：
    mutex = threading.Lock()

    #锁定
    mutex.acquire([blocking])

    #释放
    mutex.release()

其中，锁定方法acquire可以有一个blocking参数。

    如果设定blocking为True，则当前线程会堵塞，直到获取到这个锁为止（如果没有指定，那么默认为True）
    如果设定blocking为False，则当前线程不会堵塞
"""
from threading import Thread,Lock
import time

g_num = 0

def test1():
    global g_num
    # 这个线程和test2线程都在抢着对这个锁 进行上锁，
    # 如果有1方成功的上锁，那么导致另外的一方会堵塞(一直等待)到这个锁被解开为止；
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release() # 用来对mutext指向的这个锁，进行解锁，，，只
                    # 要开了锁，那么接下来会让所有因为这个锁 被上了锁 而堵塞的线程，进行抢着上锁；

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print("---test2---g_num=%d"%g_num)

# 创建一把互斥锁，这个锁默认是没有上锁的：
mutex = Lock()

p1 = Thread(target=test1)
p1.start()

# time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)


"""
# 上锁解锁过程：
    当一个线程调用锁的acquire()方法获得锁时，锁就进入“locked”状态。
    每次只有一个线程可以获得锁。如果此时另一个线程试图获得这个锁，该线程就会变为“blocked”状态，称为“阻塞”，
        直到拥有锁的线程调用锁的release()方法释放锁之后，锁进入“unlocked”状态。
    线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。

# 总结：

锁的好处：
    确保了某段关键代码只能由一个线程从头到尾完整地执行

锁的坏处：
    阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
    由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁
"""
