class CarStore(object):
    
    def order(self,car_type):
        return select_car_by_type(car_type)
        

# 利用函数解耦:
def select_car_by_type(car_type):
    if car_type == "索纳塔":
        return Suonata()
    elif car_type == "名图":
        return Mingtu()
    elif car_type == "Ix35":
        return Ix35()


class Car(object):
    def move(self):
        print("车在移动...")
    def stop(self):
        print("车在停止...")
    def music(self):
        print("正在播放音乐...") 

class Suonata(Car):
    pass 

class Mingtu(Car):
    pass 

class Ix35(Car):
    pass 

car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.music()
car.stop()



