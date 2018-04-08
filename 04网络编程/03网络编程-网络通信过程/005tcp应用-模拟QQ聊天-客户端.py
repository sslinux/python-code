from socket import *

# 创建socket
tcpClientSocket = socket(AF_INET,SOCK_STREAM)

# 链接服务器：
serAddr = ('192.168.1.9',7789)
tcpClientSocket.connect(serAddr)

while True:
    # 提示用户输入数据
    sendData = input("send:")

    if len(sendData) > 0:
        tcpClientSocket.send(sendData.encode("utf-8"))
    else:
        break

    # 接收对方发送过来的数据，最大接收1024个字节
    recvData = tcpClientSocket.recv(1024).decode("utf-8")
    print("recv:%s"%recvData)

# 关闭套接字：
tcpClientSocket.close()
