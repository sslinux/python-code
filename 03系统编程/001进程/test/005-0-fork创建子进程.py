"""
# 进程 VS 程序
编写完毕的代码，在没有运行的时候，称之为程序。
正在运行着的代码，就称为进程。
进程：除了包含代码以外，还有需要运行的环境等，所以进程和程序时有区别的。
"""

# python的os模块封装了常见的系统调用，其中就包括fork，可以在python程序中轻松创建子进程；

"""
import os

# 注意：fork函数，只在Unix/Linux/Mac上运行，Windows不可以
pid = os.fork()      

if pid == 0:
    print("哈哈1")
else:
    print("哈哈2")
"""

"""
# 运行结果：
sslinux@sslinu-pygo:~/Documents/czbk/03系统编程/001进程$ python /home/sslinux/Documents/czbk/03系统编程/001进程/005fork创建子进程.py
哈哈2
哈哈1
"""

# 说明：
"""
程序执行到os.fork()时，操作系统会创建一个新的进程(子进程),然后复制父进程的所有信息到子进程中；
然后父进程和子进程都会从fork()函数中得到一个返回值，在子进程中这个值一定是0，而父进程中是子进程的id号；
"""

# 在Unix/Linux操作系统中，提供了一个fork()系统函数，它非常特殊：
"""
普通的函数调用，调用一次，返回一次；
但是fork()调用一次，返回两次，因为操作系统自动把当前进程(称为父进程)复制了一份(称为子进程),然后分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是：一个父进程可以fork出很多子进程。所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
"""

# os.getpid()和os.getppid()

import os

rpid = os.fork()
if rpid < 0:
    print("fork调用失败。")
elif rpid == 0:
    print("我是子进程(%s),我的父进程是(%s)"%(os.getpid(),os.getppid()))
    # x += 1
else:
    print("我是父进程(%s),我的子进程是(%s)"%(os.getpid(),rpid))

print("父子进程都可以执行这里的代码")

