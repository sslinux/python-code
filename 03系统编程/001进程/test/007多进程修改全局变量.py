import os       
import time    

g_num = 100

ret = os.fork()
if ret == 0:
    print("---process-1---")
    g_num += 1 
    print("---process-1 g_num=%d---"%g_num)
else:
    time.sleep(3)
    print("---process-2---")
    print("---process-2 g_num=%d---"%g_num)

# 执行结果：
"""
sslinux@sslinu-pygo:~/Documents/czbk/03系统编程/001进程$ python /home/sslinux/Documents/czbk/03系统编程/001进程/007多进程修改全局变量.py
---process-1---
---process-1 g_num=101---
---process-2---
---process-2 g_num=100---
"""
# 进程中的代码是同一份，但数据是独立的；
# 变量在父子进程中并不共享；



