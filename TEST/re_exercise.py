"""
正则匹配练习
"""

import re

# 1. 匹配一个.com邮箱格式字符串
re1 = "12345@qq.com"
print(re.findall(r'\w+@\w+.com', re1))

# 2. 匹配一个密码 8-12位数字字母下划线构成
re2 = "1234abc78_12"
print(re.findall('\w{8,12}_?', re2))

# 3. 匹配一个数字： 正数、负数、整数、小数、分数(1/2)，百分数(45%)
# -?判断-号 \d+判断数字 /?判断/号 \.?判断.号 \d*判断数字 %?判断%号
print(re.findall(r'-?\d+/?\.?\d*%?', "12 -3 3.5 -5.45 42% 1/3"))

# 4. 匹配一段文字中以大写字母开头的单词，注意文字中可能有：
#    iPython(不算) H-base(算) 单词可能有 大写字母、小写字母以及 - _
print(re.findall(r'\b[A-Z][-_a-zA-Z]*', "Hello iPython H-base MBCC"))
