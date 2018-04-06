import os       
import time    

os.fork()
os.fork()      
os.fork()       

print("---1---")

# 死循环中去os.fork()，会无限生成子进程，会耗尽资源；被称为fork炸弹；

"""
# fork炸弹:
while True:
    os.fork()
"""
