# 正则独立于python，任何语言都要处理；；


"""
Expression，在代码中常简写为regex、regexp或RE），是计算机科学的一个概念。正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。
在很多文本编辑器里，正则表达式通常被用来检索、替换那些匹配某个模式的文本。

Regular Expression的“Regular”一般被译为“正则”、“正规”、“常规”。
此处的“Regular”即是“规则”、“规律”的意思，Regular Expression即“描述某种规则的表达式”之意。
"""

# re.match()
"""
In [1]: import re

In [2]: pattern = "itcast"

In [3]: s = "itheima"

In [4]: re.match(pattern,s)

In [5]: s = "itcast"

In [6]: re.match(pattern,s)
Out[6]: <_sre.SRE_Match object; span=(0, 6), match='itcast'>

In [7]: result = re.match(pattern,s)

In [8]: dir(result)
Out[8]: 
['__class__',
 '__copy__',
 '__deepcopy__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'end',
 'endpos',
 'expand',
 'group',
 'groupdict',
 'groups',
 'lastgroup',
 'lastindex',
 'pos',
 're',
 'regs',
 'span',
 'start',
 'string']

In [9]: result.group()
Out[9]: 'itcast'

In [10]: result = re.match("itcast","itcastitheima")

In [11]: result.group()
Out[11]: 'itcast'
"""

"""
In [12]: re.match(".","i")
Out[12]: <_sre.SRE_Match object; span=(0, 1), match='i'>

In [13]: re.match(".","\n")

In [14]: re.match("...","ab")

In [15]: re.match("...","abc")
Out[15]: <_sre.SRE_Match object; span=(0, 3), match='abc'>

In [16]: re.match("...","abcd")
Out[16]: <_sre.SRE_Match object; span=(0, 3), match='abc'>

"""

"""
In [17]: re.match("\d","1")
Out[17]: <_sre.SRE_Match object; span=(0, 1), match='1'>

In [18]: re.match("\d","a")

In [19]: re.match("\D","a")
Out[19]: <_sre.SRE_Match object; span=(0, 1), match='a'>

In [20]: re.match("\D","1")
"""

"""
In [22]: re.match("\s","\ta")
Out[22]: <_sre.SRE_Match object; span=(0, 1), match='\t'>

In [23]: re.match("\S","\ta")

In [24]: re.match("\S","a")
Out[24]: <_sre.SRE_Match object; span=(0, 1), match='a'>

"""

"""
In [25]: re.match("\w","\na")

In [26]: re.match("\w","-a")

In [27]: re.match("\w","1a")
Out[27]: <_sre.SRE_Match object; span=(0, 1), match='1'>

"""

"""
In [28]: re.match("1[34578]","18")
Out[28]: <_sre.SRE_Match object; span=(0, 2), match='18'>

In [29]: re.match("1[34578]","19")

In [30]: re.match("1[^34578]","19")
Out[30]: <_sre.SRE_Match object; span=(0, 2), match='19'>

In [31]: re.match("1[^34578]","1a")
Out[31]: <_sre.SRE_Match object; span=(0, 2), match='1a'>

In [32]: re.match("1[^34578]","18")

In [33]: re.match("1[a-z5-9]","11")

In [34]: re.match("1[a-z5-9]","19")
Out[34]: <_sre.SRE_Match object; span=(0, 2), match='19'>

\d == [0-9]
\D == [^0-9]
\w == [a-zA-Z0-9_]
"""

# 表示数量：
"""
* 匹配前一个字符出现0次或者无限次，即可有可无； 等价于：{0,}
+ 匹配前一个字符出现1次或者无限次，即至少1次； 等价于：{1,}
? 匹配前一个字符出现1次或者0次，即要么1次，要么没有； 等价于: {0,1}
{m} 匹配前一个字符出现m次
{m,} 匹配前一个字符至少出现m次；
{m,n} 匹配前一个字符出现至少m次，至多n次；
"""

"""
# 规则匹配上了，但是匹配的是空字符串，不会返回None，None只有在规则不匹配时才会被返回；
In [35]: re.match("\d*","a")
Out[35]: <_sre.SRE_Match object; span=(0, 0), match=''>

In [36]: r = re.match("\d*","a")

In [37]: r.group()
Out[37]: ''
"""

"""
In [38]: s = "\nabc"

In [39]: print(s)

abc

In [40]: s = "\\nabc"

In [41]: print(s)
\nabc

In [42]: re.match("\\\\n\w",s)
Out[42]: <_sre.SRE_Match object; span=(0, 3), match='\\na'>

In [43]: s = r"\nabc"

In [44]: s
Out[44]: '\\nabc'

In [45]: print(s)
\nabc

# 建议在正在表达式书写pattern时，建议使用r""的形式，忽略需要转义的字符；
"""


# 表示边界：
"""
^ : 匹配字符串开头；
$ ： 匹配字符串结尾；
\b : 匹配一个单词的边界；
\B : 匹配非单词边界；
"""


"""In [47]: re.match(r"^\w+ve\b","hover")

In [48]: re.match(r"^\w+\bve\b","hover")

In [49]: re.match(r"^\w+\bve\b","ho ve r")

In [50]: re.match(r"^\w+\bve\b","ho ve r")

In [51]: re.match(r"^\w+\sve\b","ho ve r")
Out[51]: <_sre.SRE_Match object; span=(0, 5), match='ho ve'>

In [52]: re.match(r"^.+ve\B","ho ve r")

In [53]: re.match(r"^.+\Bve\B","ho ve r")

In [54]: re.match(r"^.+\Bve\B","ho ver")

In [55]: re.match(r"^.+\Bve\B","hover")
Out[55]: <_sre.SRE_Match object; span=(0, 4), match='hove'>

"""

# 匹配分组：
"""
字符	        功能
|	        匹配左右任意一个表达式
(ab)	    将括号中字符作为一个分组
\num	    引用分组num匹配到的字符串
(?P<name>)	分组起别名
(?P=name)	引用别名为name分组匹配到的字符串
"""

"""In [60]: re.match(r"[1-9]\d?$|0$|100$","0")
Out[60]: <_sre.SRE_Match object; span=(0, 1), match='0'>

In [61]: re.match(r"[1-9]\d?$|0$|100$","100")
Out[61]: <_sre.SRE_Match object; span=(0, 3), match='100'>

In [62]: re.match(r"[1-9]\d?$|0$|100$","200")

In [63]: re.match(r"[1-9]\d?$|0$|100$","08")

In [64]: re.match(r"[1-9]?\d?$|100$","0")
Out[64]: <_sre.SRE_Match object; span=(0, 1), match='0'>

"""

# 分组:
"""
In [65]: re.match(r"<h1>(.*)</h1>","<h1>匹配分组</h1>")
Out[65]: <_sre.SRE_Match object; span=(0, 13), match='<h1>匹配分组</h1>'>

In [66]: result = re.match(r"<h1>(.*)</h1>","<h1>匹配分组</h1>")

In [67]: result.group()
Out[67]: '<h1>匹配分组</h1>'

In [68]: result.group(1)
Out[68]: '匹配分组'

In [69]: result = re.match(r"(<h1>)(.*)(</h1>)","<h1>匹配分组</h1>")

In [70]: result.group(1)
Out[70]: '<h1>'

In [71]: result.group(2)
Out[71]: '匹配分组'

In [72]: result.group(3)
Out[72]: '</h1>'

In [73]: result.group(0)
Out[73]: '<h1>匹配分组</h1>'

In [74]: result = re.match(r"(<h1>)(.*)(</h1>)","<h1>匹配分组</h1>")

In [75]: result.groups()
Out[75]: ('<h1>', '匹配分组', '</h1>')

"""


# \num： 引用前面分组中匹配到的字符：
"""
In [77]: s = "<html><h1>itcast</h1></html>"

In [78]: re.match(r"<(.+)><(.+)>.+</\2></\1>",s)
Out[78]: <_sre.SRE_Match object; span=(0, 28), match='<html><h1>itcast</h1></html>'>

"""


"""In [79]: p = r"(\w+)@(163|126|gamil|qq)\.(com|cn|net)$"

In [80]: r = re.match(p,"itcast@qq.com")

In [81]: r.group()
Out[81]: 'itcast@qq.com'

In [82]: r.group(1)
Out[82]: 'itcast'

In [83]: r.group(2)
Out[83]: 'qq'

In [84]: r.group(3)
Out[84]: 'com'

"""


# 分组起别名，并且引用：
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
# 注意：必须是大写的P，小写时报错(py3);

"""
In [85]: s = "<html><h1>itcast</h1></html>"

In [88]: re.match(r"<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>",s)
Out[88]: <_sre.SRE_Match object; span=(0, 28), match='<html><h1>itcast</h1></html>'>

"""