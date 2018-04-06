# if: 用来完成条件判断：

age = input("请输入你的年龄:")
# input()获取的所有数据，都当作字符串类型；

age_number = int(age)

if age_number > 18:
    print("OK")
else:
    print("Get out")

