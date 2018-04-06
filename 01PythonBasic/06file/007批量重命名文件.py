import os 
# 1、获取要重命名的文件夹 名字
folder_name = input("请输入要重命名的文件夹:")

#2、获取指定的文件夹中的所有 文件名字 
file_names = os.listdir(folder_name)

#3、重命名

os.chdir(folder_name)

for name in file_names:
    print(name)
    os.rename(name,"[www.sslinux.com]-"+name)


# import os 

# folder_name = input("Please input folder name:")

# file_names = os.listdir(folder_name)

# os.chdir(folder_name)

# for name in file_names:
#     position = name.find("-")
#     new_file_name = name[position+1:]
#     os.rename(name,new_file_name)

# os.listdir('./')
