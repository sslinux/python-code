"""
在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据；
"""


from multiprocessing import Process,Queue
import os
import time   
import random  

# 写数据进程执行的代码：
def write(q):
    for value in ['A','B','C']:
        print("Put %s to queue..." % value)
        q.put(value)      
        time.sleep(random.random())

# 读数据进程执行的代码：
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("Get %s from queue..." % value)      
            time.sleep(random.random())
        else:     # 只要队列为空了，就会结束循环；
            break   


if __name__ == "__main__":
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    # 启动子进程pw，写入：
    pw.start()
    # 等待pw结束：
    pw.join()

    # 启动子进程pr，读取：
    pr.start()
    pr.join()

    # pr进程里面是死循环，只有等消息队列为空时才会break结束；
    print("")
    print("所有数据都已经写入并且读取完毕.")