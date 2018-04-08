from socket import *
from multiprocessing import Process

def conn_ser():
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect(("192.168.1.9",7788))
    for num in range(10):
        clientSocket.send("---test---%d"%num)

def main():
    p = Process(target=conn_ser)
    p.start()


if __name__ == "__main__":
    main()
