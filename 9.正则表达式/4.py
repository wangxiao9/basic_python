'''
1. 边界值
 - ^ 开始
 - $ 结束
'''
import re

a = '109200001'
b = '10000'

# 判断当前邮箱是否符合4-8位
print(re.findall('^\d{4,8}$', a))
print(re.findall('^\d{4,8}$', b))