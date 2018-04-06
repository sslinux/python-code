# os.fork()

"""
# 过于底层，不建议使用；后面的都是对它的二次封装；
ret = os.fork()       
if ret == 0:
    # 子进程
else:
    # 父进程
"""
###################################

# Process类：

"""
from multiprocessing import Process
p1 = Process(target=xxx)
p1.start()
"""

# Pool类：
"""
from multiprocessing import Pool       
pool = Pool(3)
pool.apply_async(xxx)
# 主进程用来等待，，，真正的任务都在子进程中执行；
"""

