# coding=utf-8

"""
不修改服务器和架构代码，但要确保可以在多个架构上运行web服务器。
Python Web Server Gateway Interface,简称WSGI，读作"wizgy"

WSGI允许开发者将选择web框架和web服务器分开。
可以混合匹配web服务器和web框架，选择一个适合的配对。
比如,可以在Gunicorn 或者 Nginx/uWSGI 或者 Waitress上运行 Django, Flask, 或 Pyramid。
真正的混合匹配，得益于WSGI同时支持服务器和架构：

web服务器必须具备WSGI接口，所有的现代Python Web框架都已具备WSGI接口，它让你不对代码作修改就能使服务器和特定的web框架协同工作。

WSGI由web服务器支持，而web框架允许你选择适合自己的配对，但它同样对于服务器和框架开发者提供便利使他们可以专注于自己偏爱的领域和专长而不至于相互牵制。
其他语言也有类似接口：java有Servlet API，Ruby 有 Rack。


# 定义WSGI接口：
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello World!”：

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return 'Hello World!'

上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
    environ：一个包含所有HTTP请求信息的dict对象；
    start_response：一个发送HTTP响应的函数。

整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，把底层web服务器解析部分和应用程序逻辑部分进行了分离，这样开发者就可以专心做一个领域了

不过，等等，这个application()函数怎么调用？如果我们自己调用，两个参数environ和start_response我们没法提供，返回的str也没法发给浏览器。

所以application()函数必须由WSGI服务器来调用。
有很多符合WSGI规范的服务器。
而我们此时的web服务器项目的目的就是做一个极可能解析静态网页还可以解析动态网页的服务器
"""