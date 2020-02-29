'''
1. 正则表达式
 - re 模块
 - 匹配出来的内容以字典形式显示
 - 常用字符集 \d \D \s \S \w \W
'''
# 导入re正则表达式模块
import re

# 常用方法findall()

a = 'python|php|java|C#|ruby'
# ep1: 匹配字符串python
print(re.findall('python', a))

b = 'python1php2java3C#4ruby'
# ep2: 匹配出b中所有的数字
print(re.findall('\d', b))

# ep3: 匹配出b中所有的非字符集
print(re.findall('\D', b))

c = 'python  _php&java3C\n4ruby\r'
# ep4:匹配c中的&,空字符集
print(re.findall('\W', c))

# ep5:匹配字母下划线
print(re.findall('\w', c))

#ep6: 匹配任意空白字符
print(re.findall('\s', c))

#ep7: 匹配任意非空白字符
print(re.findall('\S', c))
