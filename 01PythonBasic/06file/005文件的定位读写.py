
f = open("test.txt")

f.seek(2,0)
# 2 表示offset;
# 0 表示whence，可取值：0,1,2（0:文件起始位置，1:当前位置，2:文件末尾)
f.read()    # read后，指针会跳到文件末尾；
f.seek(0,0) # 再次将指针调整到文件开头；

f.tell()    # 返回当前文件指针；


