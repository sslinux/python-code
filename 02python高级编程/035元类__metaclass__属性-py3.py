#-*- coding:utf-8 -*-

def upper_attr(future_class_name,future_class_parents,future_class_attr):

    # 遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value      

    # 调用type来创建一个类：
    return type(future_class_name,future_class_parents,newAttr)

class Foo(object,metaclass=upper_attr):   # 与python2的写法差异；
    bar = 'bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

f = Foo()
print(f.BAR)    # 类属性现在已经是大写的BAR了；

#######################python3，运行结果如下：###################################
"""
sslinux@sslinu-pygo:~/Documents/czbk/02python高级编程$ python /home/sslinux/Documents/czbk/02python高级编程/035元类__metaclass__属性-py3.py
False
True
bip
"""