"""
regex.py    re模块 功能函数演示
"""

import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"(\w+):(\d+)"    # 正则表达式

# re 模块调用findall
l = re.findall(pattern, s)  # 正则表达式, 字符串
print(l)    # [('Alex', '1994'), ('Sunny', '1996')]

# compile 对象调用findall
regex = re.compile(pattern)  # 在生成compile对象是写入正则表达式
l = regex.findall(s, 0, 12)  # 可截取目标字符串, 起始点, 结束点
print(l)    # [('Alex', '1994')]

"""
re.split(pattern,string,flags = 0)
功能:使用正则表达式匹配内容,切割目标字符串
参数: pattern 正则表达式
string 目标字符串
flags 功能标志位,扩展正则表达式的匹配
返回值: 切割后的内容列表
"""

# 按照正则表达式匹配内容切歌字符串
l = re.split(r'[:,]', s)    # s = "Alex:1994,Sunny:1996"
print(l)    # ['Alex', '1994', 'Sunny', '1996']

"""
re.sub(pattern,replace, string,max,flags = 0)
功能: 使用一个字符串替换正则表达式匹配到的内容
参数: pattern 正则表达式
     replace 替换的字符串
     string 目标字符串
     max 最多替换几处,默认替换全部
     flags 功能标志位,扩展正则表达式的匹配
     返回值: 替换后的字符串
"""

# 替换目标字符串
s = re.sub(r':', '-', s, 1)    # :替换- ,1替换1处，默认全部替换
print(s)    # Alex-1994,Sunny:1996
