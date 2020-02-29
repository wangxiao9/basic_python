'''
1. 匹配一组
 - []
'''

import re

a = 'ahc, abc, ddd, adc, ard, afc'

# ep1：匹配abc, afc
print(re.findall('a[bf]c', a))

# ep2：匹配非abc, afc
print(re.findall('a[^bf]c', a))

# ep3：匹配a-f 
print(re.findall('a[a-f]c', a))