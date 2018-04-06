"""
多进程复制文件

"""
from multiprocessing import Pool      
import os      

def copyFileTask(name,oldFolderName,newFolderName):
    "完成copy一个文件的功能"
    fr = open(oldFolderName + "/" + name)
    fw = open(newFolderName + "/" + name,"w")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()


def main():
    # 0、获取用户要copy的目录的名字
    oldFolderName = input("请输入你想备份的目录的名字：")
    # 1、创建一个目录
    newFolderName = oldFolderName+".bak"
    # print(newFolderName)
    os.mkdir(newFolderName)

    # 2、获取old目录中的所有的文件名字；
    fileNames = os.listdir(oldFolderName)

    # 3、使用多进程的方式copy原目录中的所有文件到新的目录中；
    pool = Pool(5)

    for name in fileNames:
        pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderName))

    pool.close()
    pool.join()
    print("文件备份完毕")

if __name__ == "__main__":
    main()















