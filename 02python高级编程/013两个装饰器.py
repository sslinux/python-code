# 定义函数，完成包裹数据
def makeBold(fn):
    def wrapped():
        print("---1---")
        return "<b>" + fn() + "</b>"
    return wrapped

# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        print("---2---")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold    # test3 = makeBold(test3)     # 后装饰
@makeItalic  # test3 = makeItalic(test3)   # 先装饰
def test3():
    print("---3---")
    return "hello world-3"

ret = test3()
print(ret)

