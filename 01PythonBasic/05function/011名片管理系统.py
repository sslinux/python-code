# 用来存储名片；
card_info = []   

def print_menu():
    """打印提示菜单"""
    print("="*50)
    print("   名片管理系统 V0.01")
    print("1:添加一个新的名片")
    print("2:删除一个名片")
    print("3:修改一个名片")
    print("4:查询一个名片")
    print("5:显示所有名片")
    print("6:退出系统")
    print("="*50)

def add_new_card_info():
    """添加一张新的名片"""
    global card_info

    new_name = input("请输入新的名字:")
    new_qq = input("请输入新的QQ:")
    new_wechat = input("请输入新的微信号:")
    new_addr = input("请输入新的住址:")

    # 定义一个新的字典，用来存储一个新的名片：
    new_info = {}
    new_info['name'] = new_name 
    new_info['qq'] = new_qq 
    new_info['wechat'] = new_wechat 
    new_info['addr'] = new_addr 

    card_info.append(new_info)   # 将一个字典添加到列表中；
    print(card_info)

def find_card_info():
    """查询名片信息"""
    global card_info

    find_name = input("请输入你像查询的姓名:")
    find_flag = 0 # 默认表示没有找到；
    for card in card_info:
        if find_name == card['name']:
            print("姓名\tQQ\t微信\t地址")
            print("%s\t%s\t%s\t%s" %(card['name'],card['qq'],card['wechat'],card['addr']))
            find_flag = 1  # 找到了就修改标识；
            break
    if find_flag == 0:
        print("Not found")

def display_card_info():
    """打印显示所有的名片信息"""
    global card_info
    print("姓名\tQQ\t微信\t地址")
    for card in card_info:
        print("%s\t%s\t%s\t%s" %(card['name'],card['qq'],card['wechat'],card['addr']))


def main():
    """该模块的主函数，控制程序的整个执行流程"""
    #1、打印功能提示：
    print_menu()

    while True:
        #2、获取用户输入：
        num = int(input("请输入操作序号:"))

        #3、根据用户的数据执行相应的功能：
        if num == 1:
            add_new_card_info()
        elif num == 2:
            pass 
        elif num == 3:
            pass 
        elif num == 4:
            find_card_info()        
        elif num == 5:
            display_card_info()
        elif num == 6:
            break
        else:
            print("输入有误，重新输入")
        print("")

if __name__ == "__main__":
    main()