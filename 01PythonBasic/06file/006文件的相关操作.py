import os 

os.rename("old_name","new_name")
os.remove("file_name")

os.mkdir("dir_name")
os.rmdir("dir_name")

os.getcwd()   # 获取当前路径；
os.chdir("../")  # 改变工作目录；
os.listdir("./")  # 获取目录下的文件；

