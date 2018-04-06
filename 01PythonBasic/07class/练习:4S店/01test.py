class CarStore(object):
    
    def order(self,money):
        if money > 50000:
            return Car()

class Car(object):
    def move(self):
        print("车在移动...")
    def stop(self):
        print("车在停止...")
    def music(self):
        print("正在播放音乐...") 

car_store = CarStore()
car = car_store.order(10000)
car.move()
car.music()
car.stop()




