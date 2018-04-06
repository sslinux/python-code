class Dog:
    
    # def __init__(self,new_name):
    #     pass 

    # 私有方法:   # 不允许在类定义之外使用；
    def __send_msg(self):
        print("----正在发送短信----")

    # 公有方法:
    def send_msg(self,new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print("余额不足，请先充值，在发送短信")

dog = Dog()
dog.send_msg(100)
