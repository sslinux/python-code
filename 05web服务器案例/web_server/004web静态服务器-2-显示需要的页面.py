# coding=utf-8

import socket
import re

from multiprocessing import Process


DOCUMENT_ROOT_DIR = "./html"

def handle_client(client_socket):
    """用一个新的进程，为一个客户端服务"""
    recv_data = client_socket.recv(1024)
    request_headlines = recv_data.splitlines()
    for line in request_headlines:
        print(line)

    http_request_headline = request_headlines[0].decode("utf-8")
    get_file_name = re.match(r"[^/]+(/[^ ]*)",http_request_headline).group(1)
    print("get_file_name is ===> %s" % get_file_name)

    if get_file_name == "/":
        get_file_name = DOCUMENT_ROOT_DIR + "/index.html"
    else:
        get_file_name = DOCUMENT_ROOT_DIR + get_file_name

    print("get_file_name is ===> %s" % get_file_name)

    try:
        f = open(get_file_name,"rb")
    except IOError:
        response_headlines = "HTTP/1.1 404 not found\r\n"
        response_headlines += "\r\n"
        response_body = "===Sorry,File Not Found==="
    else:
        response_headlines = "HTTP/1.1 200 ok\r\n"
        response_headlines += "\r\n"
        response_body = f.read()
        f.close()
    finally:
        response = response_headlines + response_body.decode("utf-8")
        client_socket.send(response.encode("utf-8"))
        client_socket.close()




def main():
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
