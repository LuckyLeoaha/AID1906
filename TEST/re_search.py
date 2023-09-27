"""
re.search()     search : 搜查，搜寻
Python的正则库re中，用来搜索匹配正则表达式第一个位置，并返回一个匹配对象，找不到匹配项，则返回None
re.search(pattern, string, flags=0)
pattern: 要匹配的正则表达式模式
string： 被搜索的字符串
flags(可选):用于修改正则的匹配方式，如忽略大小写等
"""

import re

# 规律的字符串
print(re.search(r'(ab)+', "abababababab").group())

print(re.search(r'(王|李)\w{1,3}', "王旺网wa").group())

re1 = re.search(r'(https|http|ftp|file)://\S+', "https://www.baidu.com").group()
print(re1)

# 捕获组 给子组命名为”name“
print(re.search(r'(?P<name>ab)+', "abababababab").group('name'))

# 匹配身份证号
print(re.search(r'\d{17}(\d|x)', "11009619980826105x").group())
