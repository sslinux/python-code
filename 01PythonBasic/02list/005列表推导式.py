# range(10,18,2)   ==> 返回列表； py2里：如果生成的列表元素太大，会占用较大的内存空间；
                                # py3中，使用时需要一个生成一个元素；

# list[1:10:2]

# 列表生成式：
a = [i for i in range(1,18)]

b = [11 for i in range(1,18)]  # 元素的内容由for前面的变量决定；

c = [i for i in range(10) if i%2==0]   # 生成时用if判断；

d = [i for i in range(3) for j in range(2)]
#[0,0,1,1,2,2]

e = [(i,j) for i in range(3) for j in range(2)] 

f = [(i,j,k) for i in range(3) for j in range(2) for k in range(3)]



