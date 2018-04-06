import random

while True:
    # 提示并获取用户的输入
    player = int(input("请输入 0剪刀 1石头 2布 3结束："))

    # 计算机自动生成一个：
    computer = random.randint(0,2)

    # 判断用户的输入，然后显示对应的结果：
    if player == 3:
        break
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("you win,lucky boy!")
    elif player == computer:
        print("Equal,Try again!")
    else:
        print("you lose, Haha!")
print("Game Over!")
