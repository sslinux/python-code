# 打印1到100之间的偶数：

# i = 1 
# while i <= 100:
#     if i%2 == 0:
#         print(i)
#     i += 1


# i = 1
# while i <= 5:
#     if i == 3:
#         break   # 提前结束循环；
#     print(i)

#     i += 1


i = 1 
num = 0

while i <= 100:
    if i % 2 == 0:
        print(i) 
        num += 1
    if num == 20:
        break 

    i += 1
print("There is %d numbers"% num)