# pdb是基于命令的调试工具，非常类似GNU的gdb(调试c/c++)

# python -m pdb somefile.py
"""
命令 	        简写命令 	        作用
break 	        b 	                设置断点
continue 	    c 	                继续执行程序
list 	        l 	                查看当前行的代码段
step 	        s 	                进入函数
return 	        r 	                执行代码直到从当前函数返回
quit 	        q 	                中止并退出
next 	        n 	                执行下一行
print 	        p 	                打印变量的值
help 	        h 	                帮助
args 	        a 	                查看传入参数
	            回车 	            重复上一条命令
break 	        b 	                显示所有断点
break lineno 	    b lineno 	        在指定行设置断点
break file:lineno 	b file:lineno 	    在指定文件的行设置断点
clear num 		                    删除指定断点
bt 		                            查看函数调用栈帧
"""

# l -->list， 显示当前的代码；
# n -->next,  向下执行一行代码
# c -->continue 继续执行代码
# b -->break  添加断点---> b LineNum
# clear --> 删除断点： clear index(断点的序号，使用b查看)
# p --> print 打印一个变量的值
# s --> step 进入到一个函数
# a --> args 打印所有的形参数据
# q --> quit退出调试
# r --> return 在函数中，快速执行到函数的最后一行；




# 常用调试方式：1,4
"""
1、执行时调试
	程序启动，停止在第一行等待单步调试。
	python -m pdb some.py
"""

"""
2、交互式调试：
	进入python或ipython解释器
	
import pdb
def test(a,b):
    	return a+b

pdb.run("test(11,22))
"""

"""
3、程序里埋点：
import pdb
	当程序执行到pdb.set_trace()位置时停下来调试；
"""

"""
4、日志调试：
	企业中在线服务，常用日志调试；
"""

