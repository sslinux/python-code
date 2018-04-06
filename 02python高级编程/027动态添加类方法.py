"""
动态添加类方法：
"""

class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("---%s正在吃---"%self.name)

@classmethod
def printNum(cls):
    print("---class method---")

Person.printNum = printNum    
Person.printNum()

 
