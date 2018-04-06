nums = [11,3434,54656,6768,5464323424,3425664575,12354235]
nums.sort()
print(nums)

info = [{"name":"laowang","age":10},{"name":"xiaoming","age":20},{"name":"banzhang","age":10}]

info.sort(key=lambda x:x['name'])   # 匿名函数；
print(info)