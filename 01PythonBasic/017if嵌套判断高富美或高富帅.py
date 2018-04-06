

gender = input("Please input your gender:")

if gender == "Male":
    color = input("White or not?")
    money = int(input("Please input your money."))
    beautiful = input("Beautiful or not")

    if color == "white" and money >= 1000000 and beautiful == "beautiful":
        print("白富美")
    else:
        print("黄脸婆")
elif gender == "Female":
    height = int(input("Please input your height:#cm"))
    money = int(input("Please input your money."))
    handsome = input("You are handsome or not")

    if height >= 180 and money >= 1000000 and handsome == "handsome":
        print("高富帅")
    else:
        print("矮矬穷")

