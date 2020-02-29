'''
1. 组
 - ()
'''
import re
a = 'python4python*python'

r = re.findall('(python)', a)
print(r)