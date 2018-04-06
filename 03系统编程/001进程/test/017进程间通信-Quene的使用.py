"""
Process之间需要通信，操作系统提供了很多机制来实现进程间的通信；

可以使用multiprocess模块的Quene实现多进程之间的数据传递，Quene本身是一个消息队列程序。
"""

# 队列：先进先出；

# 栈：后进先出；

from multiprocessing import Queue

q = Queue(3)     # 初始化一个Queue对象，最多可接收三条put消息；
q.put("消息1")    # 往Queue对象里添加一条消息；
q.put("消息2")
print(q.full())   # Flase # 判断Queue对象是否已经满了；
q.put("消息3")
print(q.full())   # True

# 因为消息队列已满，下面的try都会抛出异常，第一个try会等待2秒后在抛出异常，第二个try会立刻抛出异常；
try:
    q.put("消息4",True,2)
except:
    print("消息队列已满，现有消息数量:%s"%q.qsize())

try:
    q.put_nowait("消息4")
except:
    print("消息队列已满，现有消息数量:%s"%q.qsize())


# 推荐的方式，先判断消息队列是否已写满，确定未写满在写入：
if not q.full():
    q.put_nowait("消息4")

# 读取消息时，先判断消息队列是否为空，确定不为空再读取：
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())


# 说明：
"""
初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；

Queue.qsize()：返回当前队列包含的消息数量；
Queue.empty()：如果队列为空，返回True，反之False ；
Queue.full()：如果队列满了，返回True,反之False；

Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；
    1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），
        直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；
    2）如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；

Queue.get_nowait()：相当Queue.get(False)；

Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True；
1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），
    直到从消息列队腾出空间为止，如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；
2）如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；

 Queue.put_nowait(item)：相当Queue.put(item, False)；
"""

