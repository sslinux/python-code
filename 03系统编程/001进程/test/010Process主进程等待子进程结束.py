"""
使用Process创建子进程时，主进程会等待所有子进程结束后才会执行；

这个完全不同于os.fork()
"""
from multiprocessing import Process 
import time 
def test():
    for i in range(5):
        print("test")
        time.sleep(1)

p = Process(target=test)    # Process类实例化一个进程对象；target指定的代码执行完毕后，子进程结束；
p.start()    # 让这个进程开始执行test()函数里的代码；
