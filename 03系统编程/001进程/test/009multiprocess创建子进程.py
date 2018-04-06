"""
os.fork()创建子进程，只能在Unix-Like系统上执行；windows无法使用；
所以建议使用跨平台的multiprocessing模块中的Process类
"""
from multiprocessing import Process 
import time 
def test():
    while True:
        print("test")
        time.sleep(1)

p = Process(target=test)    # Process类实例化一个进程对象；target指定的代码执行完毕后，子进程结束；
p.start()    # 让这个进程开始执行test()函数里的代码；

while True:
    print("---main---")
    time.sleep(1)
