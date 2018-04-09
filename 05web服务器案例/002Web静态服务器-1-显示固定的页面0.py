# tcp socket 服务端
socket = socket.socket()
socket.bind()
socket.listen()
cli_socket = socket.accept()

whilt True:
    p = Process(target=fun,args=())
    p.start()
    cli_socket.close()

def fun(cli_socket):
    # 接收数据
    # request_data = recv()
    # print(request_data)
    # 解析HTTP报文数据:request_data
    # 提取请求方式
    # 提取请求路径:path
        HTML_ROOT_DIR = "./html"
        path = "/index.html"
        try:
            file = open('index.html')
            data = file.read()
            file.close()
        except EOError:
        """
            HTTP1.1 404 not found\r\n
            \r\n
            not found  
        """
    # 返回响应数据；
        """
        # HTTP1.1 200 ok\r\n
        # \r\n
        # hello itcast
        """
    # send()
    # close()
