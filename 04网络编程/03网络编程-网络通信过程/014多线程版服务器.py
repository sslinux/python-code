from socket import *
from multiprocessing import *
from threading import Thread
from time import sleep



# 处理客户端的请求为其服务：
def dealWithClient(newSocket,destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print("recv[%s]:%s"%(str(destAddr),recvData))
        else:
            print("[%s]客户端已经关闭"%str(destAddr))
            break
    newSocket.close()

def main():
    serSocket = socket(AF_INET,SOCK_STREAM)

    # 重复使用绑定的信息：
    # 当服务器端使用ctrl+c终止后，再次运行时，不会提示地址已经被使用；避免2WSL时间范围内地址被占用；
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    localAddr = ("",7788)
    serSocket.bind(localAddr)

    serSocket.listen(5)
    try:
        while True:
            print("---主进程，，等待新客户端的到来---")
            newSocket,destAddr = serSocket.accept()
            print("---主进程，，接下来创建一个新的进程负责数据处理[%s]----"%str(destAddr))
            # client = Process(target=dealWithClient,args=(newSocket,destAddr))
            client = Thread(target=dealWithClient,args=(newSocket,destAddr))
            client.start()

            # 因为已经向子进程中copy了一份(引用),并且父进程中这个套接字也没有用处了。
            # 所以关闭
            newSocket.close()       # 如果newSocket被close了，那么就意味着：这个套接字不能再使用recv和send来收发数据了。
    finally:
        # 当为所有的客户端服务完之后再进行关闭，表示不再接收新的客户端的链接；
        serSocket.close()

if __name__ == '__main__':
    main()
