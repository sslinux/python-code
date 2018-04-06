import os    
import time       

ret = os.fork()

if ret == 0:
    print("---子进程---")
    time.sleep(5)
    print("---子进程over---")
else:
    print("---父进程---")
    time.sleep(3)

print("---over---")

# 主进程要结束，并不会因为子进程未结束而受影响；



