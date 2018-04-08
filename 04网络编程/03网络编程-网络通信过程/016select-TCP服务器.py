# select 能够完成对一些套接字的检测；

# 1. select 原理
"""
在多路复用的模型中，比较常用的有select模型和epoll模型。
这两个都是系统接口，由操作系统提供。当然，Python的select模块进行了更高级的封装。

网络通信被Unix系统抽象为文件的读写，通常是一个设备，由设备驱动程序提供，驱动可以知道自身的数据是否可用。
支持阻塞操作的设备驱动通常会实现一组自身的等待队列，如读/写等待队列用于支持上层(用户层)所需的block或non-block操作。
设备的文件的资源如果可用（可读或者可写）则会通知进程，反之则会让进程睡眠，等到数据到来可用的时候，再唤醒进程。

这些设备的文件描述符被放在一个数组中，然后select调用的时候遍历这个数组，如果对应的文件描述符可读则会返回该文件描述符。
当遍历结束之后，如果仍然没有一个可用设备文件描述符，select让用户进程则会睡眠，直到等待资源可用的时候再唤醒，遍历之前那个监视的数组。
每次遍历都是依次进行判断的。
"""

# select回显服务器：

import select
import socket
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',7788))
server.listen(5)

inputs = [server,sys.stdin]
running = True

while True:
    # 调用select函数，阻塞等待；
    readable,writeable,exceptional = select.select(inputs,[],[])

    # 数据抵达，循环：
    for sock in readable:

        # 监听到有新的链接
        if sock == server:
            conn,addr = server.accept()
            # select 监听的socket
            inputs.append(conn)

        # 监听到键盘有输入：
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break

        # 有数据到达
        else:
            # 读取客户端连接发送的数据
            data = sock.recv(1024)
            if data:
                sock.send(data)
            else:
                # 移除select监听的socket；
                inputs.remove(sock)
    if not running:
        break

server.close()


# 3. 总结
"""
优点:
    select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点。

缺点:
    select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，
    可以通过修改宏定义甚至重新编译内核的方式提升这一限制，但是这样也会造成效率的降低。

    一般来说这个数目和系统内存关系很大，具体数目可以cat /proc/sys/fs/file-max察看。
    32位机默认是1024个。64位机默认是2048.

    对socket进行扫描时是依次扫描的，即采用轮询的方法，效率较低。

    当套接字比较多的时候，每次select()都要通过遍历FD_SETSIZE个Socket来完成调度，不管哪个Socket是活跃的，都遍历一遍。这会浪费很多CPU时间。
"""
