# 1、什么叫下载？
# 2、怎样完成下载？
#     1、创建一个空文件
#     2、向里面写数据；
#     3、关闭
# 3、什么叫上传？

# 操作码：
"""
1    读请求，即下载
2    写请求，即上传
3    表示数据包，即DATA
4    确认码，即ACK
5    错误
"""

# 4、怎么发送，怎么接收？
#     使用tftp协议
#
# 5、什么样的情况下知道了服务器发送完毕呢？
#     当客户端接收到的数据小于516(2个字节操作码+2个字节的序号+512字节数据)时，就以为着服务器发送完毕了；
#

from socket import *
import struct
import sys

if len(sys.argv) != 2:
    print("-"*30)
    print("tips:")
    print("python xxx.py 192.168.1.2")
    print("-"*30)
    exit()
else:
    ip = sys.argv[1]

# 创建udp套接字：
udpSocket = socket(AF_INET,SOCK_DGRAM)

# 构造下载请求数据：
cmd_buf = struct.pack(b"!H8sb5sb",1,b"test.jpg",0,b'octet',0)

# 发送下载文件请求数据到指定服务器：
sendAddr = (ip,69)
udpSocket.sendto(cmd_buf,sendAddr)

p_num = 0

recvFile = ""

while True:
    recvData,recvAddr = udpSocket.recvfrom(1024)
    recvDataLen = len(recvData)

    cmdTuple = struct.unpack("!HH",recvData[:4])

    cmd = cmdTuple[0]
    currentPackNum = cmdTuple[1]

    if cmd == 3:  # 判断是否为数据包；
        # 如果时第一次接收到数据，那么就创建文件；
        if currentPackNum == 1:
            recvFile = open("test.jpg","a")

        # 包编号是否和上次相等
        if p_num+1 == currentPackNum:
            recvFile.write(recvData[4:])
            p_num += 1
            print("(%d)次接收到的数据"%(p_num))

            ackBuf = struct.pack("!HH",4,p_num)

            udpSocket.sendto(ackBuf,recvAddr)
        # 如果收到的数据小于516则认为出错
        if recvDataLen < 516:
            recvFile.close()
            print("已经下载成功！!!")
            break
    elif cmd == 5: #是否为错误应答
        print("error num:%d"%currentPackNum)
        break
udpSocket.close()
