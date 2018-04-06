class Base(object):     
    def test(self):    
        print("---Base")

class A(Base):
    # pass
    def test(self):
        print("----A")

class B(Base):
    def test(self):
        print("----B")

class C(A,B):   # 多继承类；
    # pass
    def test(self):
        print("----C")

# C3算法：不需要深入
# 类名.__mro__
# 决定着调用一个方法的时候，搜索的顺序，如果在某个类中找到了方法，那么就停止搜索；

c = C()
c.test()

print(C.__mro__)

# 建议: 尽可能的不要出现相同的方法名；