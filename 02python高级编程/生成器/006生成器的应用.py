"""
利用生成器，让多个任务交替执行；   也即所谓的协程；

多任务的三种模式：
    协程
    进程
    线程
"""

def test1():
    while True:
        print("---1---")
        yield None      
    
def test2():
    while True:
        print("---2---")
        yield None       

t1 = test1()
t2 = test2()

while True:
    t1.__next__()
    t2.__next__()

