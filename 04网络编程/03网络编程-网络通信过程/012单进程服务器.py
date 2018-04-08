"""
完成一个简单的TCP服务器
并发：
并行：服务器CPU核心数大于进程数
"""

from socket import *

serSocket = socket(AF_INET,SOCK_STREAM)

# 重复使用绑定的信息：
# 当服务器端使用ctrl+c终止后，再次运行时，不会提示地址已经被使用；避免2WSL时间范围内地址被占用；
serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

localAddr = ("",7788)
serSocket.bind(localAddr)

serSocket.listen(5)


while True:
    print("---主进程，，等待新客户端的到来---")
    newSocket,destAddr = serSocket.accept()
    print("---主进程，，接下来负责数据处理[%s]---"%str(destAddr))

    try:
        while True:
            recvData = newSocket.recv(1024)
            if len(recvData) > 0:
                print("recv[%s]:%s"%(str(destAddr),recvData))
            else:
                print("[%s]客户端已经关闭"%str(destAddr))
                break
    finally:
        newSocket.close()

serSocket.close()
