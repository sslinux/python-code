ticket = 1 
knifeLength = 8 

if ticket == 1:
    print("通过车票检测，请准备安检！")

    if knifeLength <= 10:
        print("通过安检，进入候车厅")
    else:
        print("危险物品，现场没收")
else:
    print("没买票你也想回家？赶紧滚!")

