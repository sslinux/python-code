"""
如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue().
而不是multiprocessing.Queue(),否则会得到一条如下的错误信息：

RuntimeError：Queue objects should onle be shared between process through inheritance.
"""

# 示例：进程池中的进程如何通信：

#修改import中的Queue为Manager
from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))

def writer(q):
    print("writer启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "www.sslinux.com":
        q.put(i)

if __name__=="__main__":
    print("(%s) start"%os.getpid())
    q=Manager().Queue() #使用Manager中的Queue来初始化
    po=Pool()
    #使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，再用reader去读取
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) End"%os.getpid())

