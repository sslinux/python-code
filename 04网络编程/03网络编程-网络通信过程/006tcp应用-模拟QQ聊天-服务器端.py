from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET,SOCK_STREAM)

# 绑定本地信息：
address = ('',7788)
tcpSerSocket.bind(address)

# 使用socket创建的套接字默认是的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了；
tcpSerSocket.listen(5)

while True:
    # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务；
    # newSocket用来为这个客户端服务；
    # tcpSerSocket就可以空闲下来专门等待其他新客户端的链接；
    newSocket,clientAddr = tcpSerSocket.accept()

    while True:
        # 接收对方发过来的数据，最大接收1024个字节
        recvData = newSocket.recv(1024).decode("utf-8")

        # 如果接收的数据的长度为0，则意味着客户端关闭了链接
        if len(recvData) > 0:
            print("recv:%s"%recvData)
        else:
            break

        # 发送一些数据到客户端：
        sendData = input("send:")
        newSocket.send(sendData.encode("utf-8"))

    # 关闭为这个客户端服务的套接字，就意味着不能再为这个客户端服务了；
    # 如果还需要服务，只能再次重新连接；
    newSocket.close()

# 关闭坚挺套接字，这要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的连接。
tcpSerSocket.close()
