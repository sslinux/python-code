#coding=utf-8

import socket
from multiprocessing import Process


def handle_client(client_socket):
    """用一个新的进程，为一个客户端进行服务"""
    recv_data = client_socket.recv(1024).decode("utf-8")
    request_headlines = recv_data.splitlines()
    for line in request_headlines:
        print(line)

    response_headlines = "HTTP/1.1 200 ok\r\n"
    response_headlines += "\r\n"
    response_body = "hello world"

    response = response_headlines + response_body
    client_socket.send(response.encode("utf-8"))
    client_socket.close()



def main():
    """作为程序的主控制入口"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 8800))
    server_socket.listen(10)

    while True:
        client_socket, client_address = server_socket.accept()
        client_process = Process(target=handle_client, args=(client_socket,))
        client_process.start()
        client_socket.close()




if __name__ == "__main__":
    main()