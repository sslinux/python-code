"""
1.本地的进程间通信（IPC）有很多种方式，例如
    队列
    同步（互斥锁、条件变量等）

3. 什么是socket

socket(简称 套接字) 是进程间通信的一种方式，它与其他进程间通信的一个主要不同是：

它能实现不同主机间的进程间通信，我们网络上各种各样的服务大多都是基于 Socket 来完成通信的

4. 创建socket

在 Python 中 使用 socket 模块的函数 socket 就可以完成：
    socket.socket(AddressFamily, Type)
"""

# 说明：
"""
函数 socket.socket 创建一个 socket，返回该 socket 的描述符，该函数带有两个参数：
可以选择
    Address Family：
        AF_INET（用于 Internet 进程间通信）
        AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
    Type：套接字类型，可以是:
        SOCK_STREAM（流式套接字，主要用于 TCP 协议)
        SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）
"""

# 创建一个TCP套接字：
import socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')


# 创建一个UDP套接字：
import socket
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket Created')
