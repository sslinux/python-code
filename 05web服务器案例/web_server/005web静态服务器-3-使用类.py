# coding=utf-8

import socket
import sys
import re
from multiprocessing import Process

class WSGIServer(object):
    addressFamily = socket.AF_INET
    socketType = socket.SOCK_STREAM
    requestQueueSize = 5

    def __init__(self,server_address):
        """创建一个tcp套接"""
        self.listenSocket = socket.socket(self.addressFamily,self.socketType)
        # 允许重复使用上次的套接字绑定的port
        self.listenSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        # 绑定
        self.listenSocket.bind(server_address)
        # 变为被动，并制定队列的长度
        self.listenSocket.listen(self.requestQueueSize)

    def serverForever(self):
        "循环运行web服务器，等待客户端的链接并为客户端服务"
        while True:
            # 等待新客户到来
            self.client_socket, client_address = self.listenSocket.accept()

            # 方法2，多进程服务器，并发服务于多个客户端：
            new_client_process = Process(target=self.handle_request)
            new_client_process.start()

            # 因为创建的新进程中，会对这个套接字+1，所以需要在主进程中减去一次，即调用一次close()
            self.client_socket.close()

    def handle_request(self):
        "用一个新的进程，为一个客户端服务"
        recv_data = self.client_socket.recv(1024)
        request_headlines = recv_data.splitlines()
        for line in request_headlines:
            print(line)

        http_request_method_line = request_headlines[0].decode("utf-8")
        get_file_name = re.match(r"[^/]+(/[^ ]*)",http_request_method_line).group(1)
        print("get_file_name is ===>%s" % get_file_name)

        if get_file_name == "/":
            get_file_name = DOCUMENT_ROOT_DIR + "/index.html"
        else:
            get_file_name = DOCUMENT_ROOT_DIR + get_file_name

        print("get_file_name is ===>%s" % get_file_name)

        try:
            f = open(get_file_name,"rb")
        except IOError:
            response_headlines = "HTTP/1.1 404 not found\r\n"
            response_headlines += "\r\n"
            response_body = "===Sorry,File Not Found==="
        else:
            response_headlines = "HTTP/1.1 200 ok\r\n"
            response_headlines += "\r\n"
            response_body = f.read().decode("utf-8")
            f.close()
        finally:
            response = response_headlines + response_body
            self.client_socket.send(response.encode("utf-8"))
            self.client_socket.close()

# 设定服务器的端口
sever_address = (HOST,PORT) = '',8888

# 设置服务器服务静态资源时的路径：
DOCUMENT_ROOT_DIR = "./html"

def make_server(server_addr):
    server = WSGIServer(server_addr)
    return server


def main():
    global server_address
    #httpd = make_server(server_address)
    httpd = make_server((HOST,PORT))
    print("web server: Serving HTTP on prot %d..." % PORT)
    httpd.serverForever()

if __name__ == "__main__":
    main()


