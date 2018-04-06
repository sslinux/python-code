# 骡子继承自 驴和马

class Base(object):         # object类是python内置，默认继承的就是object，是所有类的老祖宗；
    def test(self):
        print("---Base")

class A(Base):
    def test1(self):
        print("----test1")

class B(Base):
    def test2(self):
        print("----test2")

class C(A,B):   # 多继承类；
    pass 

c = C()  
c.test1()
c.test2()
c.test()

