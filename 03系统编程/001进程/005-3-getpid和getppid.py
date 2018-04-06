"""
os.getpid()和os.getppid()
"""

import os

# 父进程中fork的返回值时刚刚创建出来的子进程的id；
rpid = os.fork()
if rpid < 0:
    print("fork调用失败。")
elif rpid == 0:
    print("我是子进程(%s),我的父进程是(%s)"%(os.getpid(),os.getppid()))
    # x += 1
else:
    print("我是父进程(%s),我的子进程是(%s)"%(os.getpid(),rpid))

print("父子进程都可以执行这里的代码")


# 父进程和子进程谁先执行，不确定，由操作系统调度决定；；

