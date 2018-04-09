# coding:utf-8
# 告诉解释器，当前文件的编码格式为utf-8

class Bar(object):
    pass


class Foo(object):
    """"""
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item, end=" ")
        return self

    def __str__(self):
        return "hehe"

    def say_hello(self):
        pass




print(Foo().think.different.itcast)
