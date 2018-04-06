f1 = open("test.txt","r")
line = f1.readline()
lines = f1.readlines()   # 返回一个列表，每行为一个元素；

print(line)
print(lines)
f1.close()


##################################################

old_file_name = input("请输入你想复制的文件名:")

f_old = open(old_file_name,"r")

# test.py ---> test[附件].py
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[附件]" + old_file_name[position:]

# 新建一个文件
f_new = open(new_file_name,"w+")

while True:
    content = f_old.read(1024)    # 指定每次读取1024个字节；

    if len(content) == 0:
        break
    f_new.write(content)

f_new.close()
f_old.close()




