
# 写入：
f = open("xxx.txt","w")
f.write("hahah\n")
f.write("heihei\n")

f.flush()
f.close()

############################################

# 读取：
f = open("xxx.txt","r")

content = f.read()
print(content)

f.close()
