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


"""
# 浏览器：
IE:6/7/8/10/11/edge
FireFox;Chrome
Opera
Safari
"""

"""
index.html
style --> index.css
JavaScript
    google推出JS V8引擎，大大提升了js的运行速度；
"""

"""
HTTP请求方式：
    GET：获取数据；
    POST：修改数据；
    PUT：保存数据；
    DELETE：删除数据；
    OPTION：询问服务器的某种支持特性；
    HEAD：返回报文头部信息；
"""

"""
Request Headers：
    GET / HTTP/1.1
    Host: www.baidu.com
    Connection: keep-alive
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.9
    Cookie: BAIDUID=370E396D4BF46F589D572A0903E1E7B1:FG=1; \r\n
    Content-Length:128   ==> 告诉服务器端自己发送的数据的长度；
    \r\n
    请求体：
    自行组织；
"""

"""
Response Headers:
    HTTP/1.1 200 OK
    Bdpagetype: 1
    Bdqid: 0xbb7273ce0002f434
    Bduserid: 0
    Cache-Control: private
    Connection: Keep-Alive
    Content-Encoding: gzip
    Content-Type: text/html; charset=utf-8
    Cxy_all: baidu+c8aeec072409559d56ea104aba61e202
    Date: Mon, 09 Apr 2018 01:00:43 GMT
    Expires: Mon, 09 Apr 2018 01:00:09 GMT
    Server: BWS/1.1
    Set-Cookie: BDSVRTM=0; path=/
    Set-Cookie: BD_HOME=0; path=/
    Set-Cookie: H_PS_PSSID=1431_13289_21125_26106; path=/; domain=.baidu.com
    Strict-Transport-Security: max-age=172800
    Vary: Accept-Encoding
    X-Powered-By: HPHP
    X-Ua-Compatible: IE=Edge,chrome=1
    Transfer-Encoding: chunked
"""

"""
URL：全局统一资源定位符(L:Location)

https://   schema
www.baidu.com host
/index.html   file

URI:
URN：(N:Name),在互联网中基本不怎么使用；未来趋势，但进度会很慢；
"""


"""
查询字符串：Query String
    格式：?key1=value1&key2=value2&key3=value3

HTTP协议是无状态的，
HTTP1.1 使用的是长连接
"""

"""
爬虫：spider
    避免重复；
    避免遗漏；
数据处理
"""
