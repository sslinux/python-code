"""
    同步调用就是你 喊 你朋友吃饭 ，你朋友在忙 ，你就一直在那等，等你朋友忙完了 ，你们一起去
    异步调用就是你 喊 你朋友吃饭 ，你朋友说知道了 ，待会忙完去找你 ，你就去做别的了。
"""

from multiprocessing import Pool
import time
import os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---"%i)
        time.sleep(1)
    return "hahah"

def test2(args):   # 主进程调用该回调函数的时候，会将子进程中return语句返回的值传递给回调函数；
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)

pool = Pool(3)
pool.apply_async(func=test,callback=test2)   # 回调函数test2，

while True:
    time.sleep(5)
    print("----主进程-pid=%d----"%os.getpid())
    # 我正在做自己的事，不确定子进程什么时候结束；
    # 但子进程什么时候结束，我就什么时候暂停自己的事情；
    # 去执行子进程的回调函数，然后再回来接着做自己的事情；
