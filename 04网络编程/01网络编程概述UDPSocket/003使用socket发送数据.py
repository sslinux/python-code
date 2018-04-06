from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

# 使用udp发送数据时，在每一次发送时都需要协商接收方的ip和port。
#py2
# udpSocket.sendto("haha",("192.168.1.2",8080))

#py3
udpSocket.sendto(b"haha1",("192.168.1.2",8080))
udpSocket.sendto(b"haha2",("192.168.1.2",8080))
