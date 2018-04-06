old_file_name = input("请输入你想复制的文件名:")

f_old = open(old_file_name,"r")

# test.py ---> test[附件].py
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[附件]" + old_file_name[position:]

# 新建一个文件
f_new = open(new_file_name,"w+")

content = f_old.read()
f_new.write(content)

f_new.close()
f_old.close()

