"""
查看线程数量:
threading.enumerate()
"""

import threading
from time import sleep,ctime

def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(i)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == "__main__":
    print("---开始---:%s"%ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    print(threading.enumerate())
    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数为:%d"%length)
        if length <= 1:
            break
        sleep(0.5)
