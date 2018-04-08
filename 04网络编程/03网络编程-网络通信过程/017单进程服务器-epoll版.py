# poll 解决了select套接字有上限的问题； 它和select都是使用轮询的方式进行检测；

# epoll使用的不是轮询，而是:事件通知机制；
# epoll,没有1024的限制；

# 文件描述符：fd
# fileno

"""
In [1]: import sys

In [2]: sys.stdin  # 标准输入
Out[2]: <open file '<stdin>', mode 'r' at 0x7f20c99a20c0>

In [3]: sys.stdout  # 标准输出
Out[3]: <open file '<stdout>', mode 'w' at 0x7f20c99a2150>

In [4]: sys.stderr # 标准错误
Out[4]: <open file '<stderr>', mode 'w' at 0x7f20c99a21e0>

# 文件描述符：
In [5]: sys.stdin.fileno()
Out[5]: 0

In [6]: sys.stdout.fileno()
Out[6]: 1

In [7]: sys.stderr.fileno()
Out[7]: 2
"""

# select.EPOLLIN：判断事件是否是接收数据的事件；


# 1、epoll的优点：
"""
    1、没有最大并发连接的限制，能打开的FD(指的是文件描述符，通俗的理解就是套接字对应的数字编号)的上限远大于1024.abs
    2、效率上升，不是轮询的方式，不会随着FD书目的增加效率下降。只有活跃可用的FD才会调用callback()函数；
        即epoll最大的优点就在于它只管你"活跃"的连接，而跟连接总数无关，因此在实际的网络环境中，epoll的效率就会远远高于select和poll。
"""

# epoll使用参考代码：

import socket
import select

# 创建套接字：
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 设置可以重复使用绑定的信息：
s.setsockopt(socket.SOL_SOCKET,socket.REUSEADDR,1)

# 绑定本机信息：
s.bind(("",7788))

# 变为被动：
s.listen(10)

# 创建一个epoll对象
epoll = slelect.epoll()

# 测试，用来打印套接字对应的文件描述符
# print s.fileno()
# print select.EPOLLIN|select.EPOLLET

# 注册事件到epoll中
# epoll.register(fd[, eventmask])
# 注意，如果fd已经注册过，则会发生异常

# 将创建的套接字添加到epoll的事件监听中
epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

connections = {}
address = {}

# 循环等待客户端的到来或者对方发送数据：
while True:
    # epool进行fd扫描的地方 --- 未指定超时时间则为阻塞等待；
    epoll_list = epoll.poll()

    # 对事件进行判断
    for fd,events in epoll_list:
        print(fd)
        print(events)

        # 如果是socket创建的套接字被激活：
        if fd == s.fileno():
            conn,addr = s.accept()

            print("有新的客户端到来:%"%str(addr))

            # 将conn和addr信息保存起来；
            connections[conn.fileno()] = conn
            address[conn.fileno()] = addr

            # 向epoll中注册连接socket的可读事件
            epoll.register(conn.fileno(),select.EPOLLIN|select.EPOLLET)

        elif events == select.EPOLLIN:
            # 从激活fd上接收
            recvData = connections[fd].recv(1024)

            if len(recvData) > 0:
                print("recv:%s"%recvData)
            else:
                # 从epoll中移除该连接 fd
                epoll.unregister(fd)

                # server 则主动关闭该连接 fd
                connections[fd].close()

                print("%s---offline---"%str(address[fd]))

# 2.说明：
"""
EPOLLIN 可读
EPOLLOUT 可写
EPOLLET ET模式

epoll对文件描述符的操作有两种模式：LT(level trigger) 和 ET(edge trigger).
LT模式是默认模式，LT模式与ET模式的区别如下：

LT模式：
    当epoll检测到描述符事件发生并将此事件通知应用程序，
    应用程序可以不立即处理该事件，下次调用epoll时，会再次响应应用程序通知此事件；

ET模式：
    当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。
    如果不处理，下次调用epoll时，不会再响应应用程序并通知此事件。

"""
