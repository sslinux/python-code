IDE:集成开发环境，集成了编写、运行、调试等功能于一身；

创建项目时需要自行指定解释器；

pycharm会自动提示所有不符合PEP8规范的代码；

新式类和旧式类的区别：
    python3中都是新式类；python2中有旧式类；

```python
#旧式类
class A:
    def __init__(self):
    a = 10
    
class B(A):
    def __init__(self):
        pass
        
class C(A):
    pass
```

**建议定义类时，继承自object类；** 

### 查找属性的顺序：

```python

class Foo(object):
    cls_pro = 10
    @classmethod
    def c_met(cls):
        pass

    def __init__(self):
        self.obj_pro = 11
        
    def __getattr__(self, item):
        print(item)
        return self
    
    def __getattribute__(self, item):
        pass 
    
    def __str__(self):
        return ""
    
    def say_hello(self):
        pass 
        
# 实例化对象：
foo = Foo()

print(foo.__dict__)
print(foo.obj_pro)    # 查找foo.__dict__所返回的字典中有没有以"obj_pro"为key的元素；

print(Foo.__dict__)
print(foo.cls_pro)   # 先查找foo.__dict__,在查找Foo.__dict__;

if "it" not in foo.__dict__.keys() and "it" not in Foo.__dict__.keys():
    print("*"*10)
    print("No this attribute.")
else:
    print(foo.it)         # 先查找foo.__dict__,在查找Foo.__dict__; 如果都找不到则报错；
    
    
# 如果上述两个魔法字典中都不能找到属性，则调用__getattr__()方法；
```


‵‵‵python

    def __getattribute__(self, item):
        # 该方法不建议重写；
        # 该方法定义的是：点号运算符涉及到的属性的查找顺序；
        pass
```

