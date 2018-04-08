"""
应用层
传输层：tcp/udp
网络层
链路层
"""

"""
# 伪代码：
socket = socket.socket(AF_INET,SOCK_STREAM|SOCK_DGRAM)
socket.bind()
socket.listen()
cli_so = socket.accept()
so.send()
so.recv()
socket.close() # 四次挥手；
"""
