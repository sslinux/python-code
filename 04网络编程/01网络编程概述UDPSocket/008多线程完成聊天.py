
from threading import Thread
from socket import *


# 1.收数据，然后打印

def recvData():
    recvInfo = udpSocket.recvfrom(1024)
    print("\r>>%s:%s\r"%(str(recvInfo[1]),recvInfo[0].decode("gb2312")))



# 2.检测键盘，发数据
def sendData():
    while True:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode("gb2312"),(destIp,destPort))

udpSocket = None
destIp = ""
destPort = 0


def main():

    global udpSocket
    global destIp
    global destPort

    destIp = input("对方的ip:")
    destPort = int(input("对方的port:"))
    localPort = int(input("本地的Port:"))
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",localPort))

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == "__main__":
    main()
