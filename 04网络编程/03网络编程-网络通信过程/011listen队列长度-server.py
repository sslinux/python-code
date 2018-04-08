# 服务器端存在两个队列：
    # 1、半连接队列：未收到客户端的二次ACK请求；
    # 2、已连接队列：已收到客户端的二次ACK请求；

# 连接建立成功后会从半连接队列添加到已连接队列；；


# listen(5)中，5表示的就是上述这个队列的长度和；
# 但在linux中，这个值不会生效，会按照Linux内核中的设置生效；

from socket import *
from time import sleep

# 创建socket
tcpSerSocket = socket(AF_INET,SOCK_STREAM)

# 绑定本地信息：
address = ("",7788)
tcpSerSocket.bind(address)

connNum = int(input("请输入最大的链接数:"))

# 使用sokcet创建的套接子默认的属性是主动的，使用listen将其转变为被动的，这样就可以接收别人的链接了。
tcpSerSocket.listen(connNum)

while True:
    # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器；
    newSocket,clientAddr = tcpSerSocket.accept()
    print(clientAddr)
    sleep(1)
