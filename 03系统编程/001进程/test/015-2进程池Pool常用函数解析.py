"""
multiprocessing.Pool常用函数解析：
    apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；

    apply(func[, args[, kwds]])：使用阻塞方式调用func

    close()：关闭Pool，使其不再接受新的任务；

    terminate()：不管任务是否完成，立即终止；

    join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；
"""
