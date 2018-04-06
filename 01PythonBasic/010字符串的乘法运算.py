# 使用input()获取必要的信息
name = input("请输入名字：")
high = int(input("请输入您的身高："))
# py2 中的input()是将输入的内容当成python语句去执行，
# py2中要想将输入的内容当成字符串赋值给变量，需要使用raw_input()

# 使用print来打印名片信息：
print("="*20)
print("姓名：%s"%name)
print("身高：%d"%high)
print("="*20)