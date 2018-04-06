# 1、打印功能提示
print("="*50)
print("   名字管理系统 V8.6")
print("1:添加一个新的名字")
print("2:删除一个名字")
print("3:修改一个名字")
print("4:查询一个名字")
print("5:退出系统")
print("="*50)

names = []   # 定义空列表，用来存储添加的名字；

while True:
    # 2、获取用户选择 
    num = input("请输入功能序号：")
    if num.isdigit():
        num = int(num)
    else:
        print("请您按照提示输入1-5的数字，谢谢合作")
        continue 
    

    # 3、根据用户的选择，执行相应的功能
    if num == 1:
        new_name = input("请输入名字:")
        names.append(new_name)
        if new_name in names:
            print("%s添加成功!"%new_name)
        print(names)
    elif num == 2:
        del_name = input("请输入你要删除的名字:")
        if del_name in names:
            names.remove(del_name)
        else:
            print("对不起！你要删除的名字并不存在！") 
    elif num == 3:
        old_name = input("请输入原来的名字：")
        if old_name in names:
            mod_name = input("请输入您的新名字：")
            old_index = names.index(old_name)
            names[old_index] = mod_name 
        else:
            print("你输入的名字并不存在，请核实。")
    elif num == 4:
        find_name = input("请输入你要查询的名字：")
        if find_name in names:
            print("找到了你要找的人")
        else:
            print("查无此人！")
    elif num == 5:
        break
    else:
        print("您的输入有误，请重新输入")