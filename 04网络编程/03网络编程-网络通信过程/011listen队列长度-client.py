from socket import *

connNum = input("请输入要链接服务器的次数:")
for i in range(int(connNum)):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(("192.168.1.9",7788))
    print(i)
