nums = [11,22,33,44]

for temp in nums:
    print(temp)
else:                   # 当for循环正常结束后，才执行else后面的语句；若循环中break了，则不会执行；
    print("="*10)



card_info = [{"name":"laowang","age":18},{"name":"laoli","age":18},{"name":"laozhao","age":28}]
find_name = input("请输入你想要查找的名字:")

for temp in card_info:
    if temp['name'] == find_name:
        print("找到了...")
        break 
else:
    print("没有找到....")