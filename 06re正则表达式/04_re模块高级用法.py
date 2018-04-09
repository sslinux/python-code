import re


# search(),从左往右，只匹配一个；
"""
In [89]: s = "<html><h1>itcast</h1></html>"

In [90]: re.search(r"itcast",s)
Out[90]: <_sre.SRE_Match object; span=(10, 16), match='itcast'>

In [91]: re.search(r"^itcast$",s)

In [92]: re.search(r"^itcast",s)

In [93]: s = "itcast</h1></html>"

In [94]: re.search(r"^itcast",s)
Out[94]: <_sre.SRE_Match object; span=(0, 6), match='itcast'>
"""

# findall()   # 匹配所有；

# sub()  将匹配到的数据进行替换；
"""
In [95]: re.sub(r"php","python","itcast python cpp php python php")
Out[95]: 'itcast python cpp python python python'

In [96]: re.sub(r"\d+","50","python=1000,php=0")
Out[96]: 'python=50,php=50'

In [97]: def replace(result):
    ...:     print(result.group())
    ...:     return "50"
    ...: 
    ...: 

In [98]: re.sub(r"\d+",replace,"python=1000,php=0")
1000
0
Out[98]: 'python=50,php=50'

In [99]: def replace(result):
    ...:     print(result.group())
    ...:     r = int(result.group()) + 50    # 要将匹配到的字符转换为int后才能执行加法运算；
    ...:     return str(r)    # 返回的值必须转换为字符串；
    ...: 
    ...: 

In [100]: re.sub(r"\d+",replace,"python=1000,php=0")
1000
0
Out[100]: 'python=1050,php=50'
"""

"""
In [1]: s = '''<div>
   ...:         <p>岗位职责：</p>
   ...: <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
   ...: <p><br></p>
   ...: <p>必备要求：</p>
   ...: <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
   ...: <p>&nbsp;<br></p>
   ...: <p>技术要求：</p>
   ...: <p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
   ...: <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
   ...: <p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
   ...: <p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
   ...: <p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
   ...: <p>&nbsp;<br></p>
   ...: <p>加分项：</p>
   ...: <p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
   ...: 
   ...:         </div>'''


In [3]: import re

In [4]: re.sub(r"<.+>","",s)   # 因为贪婪模式导致的；
Out[4]: '\n        \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n        '

In [5]: re.sub(r"</?\w+>","",s)  # 这个的效果就正常多了；

"""

# split 根据匹配进行切割字符串，并返回一个列表；

"""
In [101]: s = "itcast:php,python,cpp-java"

In [102]: re.split(r":|,|-",s)
Out[102]: ['itcast', 'php', 'python', 'cpp', 'java']
"""

# re的贪婪模式：

"""
In [12]: s1 = "This is a number 234-235-22-423"

In [13]: type(s1)
Out[13]: str

In [14]: re.match(r".+(\d+-\d+-\d+-\d+)",s1)
Out[14]: <_sre.SRE_Match object; span=(0, 31), match='This is a number 234-235-22-423'>

In [15]: r = re.match(r".+(\d+-\d+-\d+-\d+)",s1)

In [16]: r.group(1)
Out[16]: '4-235-22-423'

In [17]: r = re.match(r"(.+)(\d+-\d+-\d+-\d+)",s1)

In [18]: r.groups()
Out[18]: ('This is a number 23', '4-235-22-423')

In [19]: r = re.match(r"(.+?)(\d+-\d+-\d+-\d+)",s1)  # 在数量描述符的后面紧跟？,关闭它的贪婪模式；
# 但是，关闭贪婪模式时，也要考虑后面的模式匹配，需要优先考虑被关闭贪婪模式后面的表达式；

In [20]: r.groups()
Out[20]: ('This is a number ', '234-235-22-423')

"""

'''
In [21]: s = """<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display
    ...: : inline;">
    ...: """

# 如果匹配时得到的结果要大于自己预想的，第一反应应该是贪婪模式在作怪；
In [22]: re.search(r"https.+\.jpg",s).group()
Out[22]: 'https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg'

In [23]: re.search(r"https.+?\.jpg",s).group()
Out[23]: 'https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg'

In [25]: re.findall(r"https.+?\.jpg",s)
Out[25]: 
['https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg',
 'https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg']
 
'''

# 练习：

# 1、提取网站地址：
"""
In [26]: s = "http://www.interoem.com/messageinfo.asp?id=35"

In [27]: re.sub(r"http://.+?/","",s)
Out[27]: 'messageinfo.asp?id=35'

In [28]: re.sub(r"http://.+?/(.*)","",s)
Out[28]: ''

In [29]: re.sub(r"(http://.+?/).*",lambda x:x.group(1),s)
Out[29]: 'http://www.interoem.com/'
"""

# 找出单词：

"""
In [30]: s = "hello world ha ha"

In [31]: s.split()
Out[31]: ['hello', 'world', 'ha', 'ha']

In [37]: re.findall(r"\b[a-zA-Z]+\b",s)
Out[37]: ['hello', 'world', 'ha', 'ha']

"""

