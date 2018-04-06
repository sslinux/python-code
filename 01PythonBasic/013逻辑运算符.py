'''
or      或者
and     并且
not     非
'''

score = int(input("Please input your score:"))

if score > 100 or score < 0:
    print("It's not impossible!")
elif score >= 80 and score <= 100:
    print("You can get A!")
elif not score < 60:
    print("You can get B!")
else:
    print("You are so stupid!")

# if 注意点：
# 条件满足时，需要执行的多条语句，缩进需要相同；

sex = input("please input your gender:")

if sex == "Male":
    print("You are a man or boy!")
elif sex == "Female":
    print("You are a woman or girl!")
else:
    print("Please leave my country!")

