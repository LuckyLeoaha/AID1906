"""
正则表达式
"""

import re

p = re.findall("ab|cd", "abcdefgh")  # | 或
print(p)  # ['ab', 'cd']

p = re.findall("张.", "张三李四")  # . 表示任意一个字符
print(p)  # ['张三']

p = re.findall("[a-z0-9]", "AaBbCc0123")  # 区间 a-z 0-9
print(p)  # ['a', 'b', 'c', '0', '1', '2', '3']

# [^] 中括号内的^ 表示包含的字符取反（去掉）
p = re.findall("[^aeiou]", "hello world")
print(p)  # ['h', 'l', 'l', ' ', 'w', 'r', 'l', 'd']

# 元字符:^ 匹配字符串开始位置
p1 = re.findall("^Jame", "he,Jame,hello")
p2 = re.findall("^Jame", "Jame,hello")
print(p1)  # []  Jame不在开头,获取不到
print(p2)  # ['Jame']  Jame在开头

# 元字符：$ 匹配目标字符串的结尾位置
p1 = re.findall("Jame$", "Hi,Jame")
p2 = re.findall("Jame$", "Jame,welcome")
print(p1)  # ['Jame']  Jame在末尾
print(p2)  # []  Jame不在末尾

# ^和$必然出现在正则表达式的开头和结尾
# 如果同时出现，则中间部分必须完全匹配目标字符串
p = re.findall("^Jame$", "Jame")
print(p)  # ['Jame'] 反之为[]

# 元字符：* 匹配前面的字符出现0次或多次
p = re.findall("wo*", "wooooo~~w!abc")  # *只管左边1位字符，代表匹配0个或多个o，
print(p)  # ['wooooo', 'w'] # o*匹配wooooo w匹配w

p = re.findall("[a-zA-Z]*", "How are you?")
print(p)  # ['How', '', 'are', '', 'you', '', '']

p = re.findall("[0-9]*", "I'm 18")
print(p)  # ['', '', '', '', '18', '']

# 匹配大写字母开头的单词
p = re.findall("[A-Z][a-z]*", "How are you? Fine Jame")
print(p)  # 满足大写，满足小写，*通配符

# 元字符：+ 匹配前面的字符出现1次或多次
p = re.findall("[A-Z][a-z]+", "I am good, Im boy")
print(p)  # ['Im'] 单个字符 + 匹配不到

# 元字符：? 匹配前面的字符出现0次或1次
p = re.findall("-?[0-9]+", "167 -28 29 -8")
print(p)  # ['167', '-28', '29', '-8']

p = re.findall("[^ ]+", "Port-9 Error #404# %@STD")
print(p)

# 元字符：{n}   匹配前面的字符出现n次
p = re.findall("ab{3}", "abcdabbbbbbbbbbb")
print(p)  # ['abbb']
# 匹配国内手机号 1开头+10位数字
p = re.findall("1[0-9]{10}", "张三:13846524719")
print(p)  # ['13846524719']
p = re.findall("^.{3}1[0-9]{10}", "张三:13846524719")
print(p)  # ['张三:13846524719']
p = re.findall("张.{3}", "张三四五")
print(p)  # ['张三四五']

# 元字符：{m,n}  匹配前面的字符出现m-n次
p = re.findall("ab{2,4}", "abcdeabbbbbbb")
print(p)  # ['abbbb']
# 匹配QQ号
p = re.findall("[1-9][0-9]{5,10}", "qq:5626666")
print(p)  # ['405375149'] 第一位[1-9]第二位[0-9]重复出现次数{5到10次}

# 元字符： \d 匹配任意数字字符  \D 匹配任意非数字字符
p = re.findall("\d{1,5}", "Mysql: 3306, http:80")   # 匹配1-5位数
print(p)    # ['3306', '80']
p = re.findall("\D+", "Mysql: 3306, http:80")
print(p)    # ['Mysql: ', ', http:']

# 元字符： \w 匹配任意普通字符  \W 匹配任意非普通字符
# 说明：普通字符指数字，字母，下划线，汉字，普通utf-8
p = re.findall("\w+", "server_port = 8888")
print(p)    # ['server_port', '8888']
p = re.findall("\W+", "server_port = 8888")
print(p)    # [' = ']
p = re.findall("\w+", "谢谢 ありがとうございます ")
print(p)    # ['谢谢', 'ありがとうございます']

# 元字符： \s 匹配空字符  \S 匹配非空字符
p = re.findall("\w+\s+\w+", "hello    world")   # \w+匹配字符 \s+匹配空字符
print(p)    # ['hello    world']
p = re.findall("\S+", "hello     world")    # \S+匹配非空字符
print(p)    # ['hello', 'world']

# 元字符： \A 表示开头位置    \Z 表示结尾位置
p1 = re.findall("\Ahello", "hello world")
p2 = re.findall("world\Z", "hello world")
print(p1)   # ['hello']  \A 同 ^
print(p2)   # ['world']  \Z 同 $

# 元字符： \b 表示单词边界   \B 表示非单词边界
# 说明：单词边界指数字字母（汉字）下划线与其他字符的交界位置
p1 = re.findall("is", "This is a test")
p2 = re.findall(r"\bis\b", "This is a test")
print(p1)   # ['is', 'is']
print(p2)   # ['is']    加r代表原始字符串
p1 = re.findall(r'\d+', "123 65 Num007")    # 取数字
p2 = re.findall(r'\b\d+\b', "123 65 Num007")    # 取数字，不要007
print(p1)   # ['123', '65', '007']
print(p2)   # ['123', '65']

# 如果使用正则表达式匹配特殊字符，则需要加 \ 表示转义
# 特殊字符： .*+?^$[](){}|\
p = re.findall('\d+\*+\d+', "2**16")
print(p)    # ['2**16']
p = re.findall('-?\\d+\\.?\\d*', "12 -36 28 1.34 -3.8")
print(p)    # ['12', '-36', '28', '1.34', '-3.8']  -?判断- \d+ 数 \.特殊符号 \d* 数

p = re.findall('\\$\\d+', "日薪：$100")
print(p)    # ['$100']

p1 = re.findall('\bis\b', "This is a test.")
p2 = re.findall('\\bis\\b', "This is a test.")
print(p1)    # []
print(p2)    # ['is']   # 转义后

p = re.findall('\S', "\\")    # 匹配 \  \S = \\\\
print(p)    # ['\\']

# r 原生字符串 使用原生字符串书写正则表达式避免多重转义的麻烦
p1 = re.findall('\\bis\\b', "This is a test")
p2 = re.findall(r'\bis\b', "This is a test")
print(p1)   # ['is']
print(p2)   # ['is']

s = "[花千骨],[陆贞传奇],[新还珠格格],[楚乔传]"
p = re.findall(r'\[.+?\]', s)
print(p)

p = re.findall(r'\(.+?\)', "(abcd)efgh(higk)")
print(p)
