from socket import *

def main():
    udpSocket = socket(family=AF_INET,type=SOCK_DGRAM)
    udpSocket.bind(("",6789))

    num = 1
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        udpSocket.sendto(recvInfo[0],recvInfo[1])
        print("已经将接收到的第%d个数据返回给对方,内容为:%s"%(num,recvInfo[0].decode("gb2312")))
        num += 1
        # print("[%s]:%s"%(str(recvInfo[1]),recvInfo[0].decode("gb2312")))

if __name__ == "__main__":
    main()
