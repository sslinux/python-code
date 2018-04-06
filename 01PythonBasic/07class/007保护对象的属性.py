#隐藏(保护)对象的属性:


class Dog:
    def set_age(self,new_age):    # 建议将设置属性和获取属性的操作通过方法来实现；
        if new_age > 0 and new_age <= 100:
            self.age = new_age 
        else:
            self.age = 0

    def get_age(self):
        return self.age 


dog = Dog()
# dog.age = -10

# dog.name = "小白"
dog.set_age(-10)
age = dog.get_age()
print(age)

# dog.get_age()
# dog.get_name()

