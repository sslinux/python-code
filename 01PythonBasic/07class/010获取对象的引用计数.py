import sys 

a = 10

sys.getrefcount(a)             # 测量对象的引用计数,比实际的引用计数通常要大1；


class T:
    pass 

t = T()

print(sys.getrefcount(t))
