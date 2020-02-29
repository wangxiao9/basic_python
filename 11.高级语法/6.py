'''
1. reduce
 - 求和
 - 接收一个函数，序列，还有个初始值（可以有可以无）
'''
# 需要从functools 包中导入reduce
from functools import reduce

list_x = [1,2,3,4,5,6]

# reduce 相当于计算1+2+3+4+5+6 的和
r1 = reduce(lambda x,y:x+y, list_x)
print(r1)

# 第三个参数可以设置为初始值,初始值从2开始
r2 = reduce(lambda x,y:x+y, list_x, 2)
print(r2)