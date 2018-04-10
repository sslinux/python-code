# 如果a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数),如果求出a、b、c可能的组合；

# 思路：枚举法；

import time

start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print("a:%s,b:%s,c:%s" % (a,b,c))
end_time = time.time()
print("times:%d" % (end_time-start_time))
print("finished")

# 运行结果：
"""
/home/sslinux/Documents/python-code/08数据结构和算法/venv/bin/python /home/sslinux/Documents/python-code/08数据结构和算法/01引入.py
a:0,b:500,c:500
a:200,b:375,c:425
a:375,b:200,c:425
a:500,b:0,c:500
times:88
finished
"""

"""
算法是独立存在的一种解决问题的方法和思想。

算法的五大特性
    1、输入: 算法具有0个或多个输入
    2、输出: 算法至少有1个或多个输出
    3、有穷性: 算法在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成
    4、确定性：算法中的每一步都有确定的含义，不会出现二义性
    5、可行性：算法的每一步都是可行的，也就是说每一步都能够执行有限的次数完成
"""