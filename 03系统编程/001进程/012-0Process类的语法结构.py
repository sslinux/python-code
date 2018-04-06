from multiprocessing import Process
import os

# 子进程要执行的代码：
def run_proc(name):
    print("子进程运行中，name=%s,pid=%d..." % (name,os.getpid()))

if __name__ == "__main__":
    print("父进程 %d" % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print("子进程将要执行")
    p.start()
    p.join()
    print("子进程已结束")

# 说明：
"""
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动；
join()方法可以等待子进程结束后在继续往下运行，通常用于进程间的同步。
"""

# Process语法结构：
"""
Process([group [,target [,name [,args,[kwargs]]]]])

target: 表示这个进程实例所调用对象；
args：表示调用对象的位置参数元组；
kwargs:表示调用对象的关键字参数字典；
name： 为当前进程实例的别名；
group：大多数情况下用不到；
"""

# Process类常用方法：
"""
is_alive():判断进程实例是否还在执行；
join([timeout]): 是否等待进程实例执行结束，或等待多少秒；
start():启动进程实例(创建子进程);
run(): 如果没有给定target参数，对这个对象调用start()方法时，就将执行对象中的run()方法；
terminate():不管任务是否完成，立即终止；
"""

# Process类常用属性：
"""
name: 当前进程实例别名，默认为Process-N，N为从1开始递增的整数；
pid: 当前进程实例的PID值；
"""

