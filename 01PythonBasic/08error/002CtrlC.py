import time 

try:
    while True:
        print("哈哈！")
        time.sleep(2)
except KeyboardInterrupt as e:
    print("用户主动终止了程序的运行!")
    print(e)
except Exception as e_info:
    print(e_info)
else:
    print("此处无错误，恭喜！")
finally:
    print("赶紧弄完，好去吃饭！")