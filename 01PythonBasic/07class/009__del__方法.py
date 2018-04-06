class Dog:
    def __del__(self):              # 当对象的引用计数为0时，python解释器会自动执行该方法；
        print("----英雄over----")


dog1 = Dog()
dog2 = dog1 

del dog1 
del dog2
print("="*10)
# 如果程序执行过程中，对象的引用计数就已经为零了的话，__del__方法就会执行；
# 如果程序执行到最后一行，贵像的引用计数依然不为零，在程序结束时，python解释器将自动清零对象的引用计数，释放内存空间，此时也会调用__del__方法；

