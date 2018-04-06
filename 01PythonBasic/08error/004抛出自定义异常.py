
class ShortInputException(Exception):
    """自定义的异常类"""

    def __init__(self,length,atleast):
        # super().__init__()
        self.length = length 
        self.atleast = atleast

def main():
    try:
        s = input("请输入 -->")
        if len(s) < 3:
            # raise引发一个自定义的异常
            raise ShortInputException(len(s),3)
    except ShortInputException as result:  # result这个变量被绑定到了异常返回的 实例对象；
        print("ShortInputException:输入的长度是 %d,长度至少应该是 %d"%(result.length,result.atleast))
    else:
        print("没有异常发生。")

if __name__ == "__main__":
    main()