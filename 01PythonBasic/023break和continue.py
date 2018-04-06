# i = 1
# while i <= 10:
#     print("-"*10)
#     if i == 2:
#         break   # 结束循环；
#     print(i)
#     i += 1
# print("="*10)


i = 1
while i <= 10: 
    i += 1
    if i == 5:
        continue   # 跳过本次循环
    print("-"*10)
    print(i)
print("="*10)