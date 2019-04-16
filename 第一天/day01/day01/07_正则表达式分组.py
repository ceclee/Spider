'''正则表达式分组'''
import re

s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))

# 1.先按照整体匹配:['A B','C D']
# 2.匹配分组内容,如果有2个以上分组,
# 　则以元组形式显示
#   [('A','B'),('C','D')]






