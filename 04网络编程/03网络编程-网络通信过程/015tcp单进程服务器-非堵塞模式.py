# Web服务器使用多进程、多线程的原因：
# 如果没有多进程、多线程，那么任务是单任务的，即在为一个顾客服务的时候，不能为其他顾客服务；

from socket import *

# 1、创建套接字
serSocket = socket(AF_INET,SOCK_STREAM)

serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 2、绑定本地ip以及port：
localAddr = ("",7788)
serSocket.bind(localAddr)

# 3、让这个socket变为非杜塞：
serSocket.setblocking(False)

# 3、将socket变为监听(被动)套接字
serSocket.listen(100)

# 用来保存所有已经连接的客户端的信息：
clientAddrlist = []

while True:
    # 等待一个新的客户端的到来(即完成3次握手的客户端)
    try:
        newSocket,destAddr = serSocket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来:%s"%str(clientAddr))
        clientSocket.setblocking(False)
        clientAddrlist.append((clientSocket,clientAddr))

    for clienSocket,clientAddr in clientAddrlist:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData) > 0:
                print("%s:%s"%(str(clientAddr),recvData))
            else:
                clientSocket.close()
                clientAddrlist.remove((clientSocket,clientAddr))
                print("%s 已经下线"%clientAddr)
