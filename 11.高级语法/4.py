'''
1. 匿名函数
 - lambda 关键字标识匿名函数
'''

# 普通函数
def add(x,y):
    return x + y

print(add(1,2))

# 匿名函数 lambda表达式，x,y 对应的add(x,y) 函数里的形参，中间用：冒号
r = lambda x,y : x + y
print(r) # <function <lambda> at 0x107c1ebf8>
print(r(1,2))