import os
import time    

ret = os.fork()     # os.fork()在子进程中的返回值为0；父进程中的返回值为子进程的pid。
if ret == 0:
    while True:
        print("---1---")
        time.sleep(1)
else:
    while True:
        print("---2---")
        time.sleep(1)

