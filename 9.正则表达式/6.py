import re

'''
ep1: 匹配 I love you
'''
a = 'Python I love you too'

r1 = re.findall('Python\s(.*?)\stoo', a)
print(r1)
