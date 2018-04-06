"""
动态地创建类：
    类也是对象，可以在运行时动态地创建他们，就像其他对象一样；
"""

def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass        
        return Foo    # 返回的是类，不是类的实例；
    else:
        class Bar(object):
            pass 
        return Bar
    
MyClass = choose_class('foo')
print(MyClass)    # 函数返回的是类，不是类的实例；

print(MyClass())   # 你可以通过这个类来创建实例，也就是实例对象；

