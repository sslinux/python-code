from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect(("192.168.1.2",8989))

# 注意：
# 1、tcp客户端已经连接好了服务器，所以在以后的数据发送中，不需要填写对方的ip和port；
# 2、udp在发送数据的时候，因为没有之前的链接，所以需要在每次的发送中，都要填写接收对方的ip和port
clientSocket.send("haha".encode("gb2312"))

recvData = clientSocket.recv(1024)
print("recvData:%s"%recvData)

clientSocket.close()
