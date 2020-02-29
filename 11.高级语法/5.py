'''
1. map
 - 接收两个参数，一个函数，一个序列
 - 返回的还是一个序列
'''

list_x = [1,2,3,4,5]

def factory(x):
    return x * x

r1 = map(factory, list_x)
print(list(r1))
# 结合lambada
r2 = map(lambda x : x * x, list_x)
print(list(r2))

# 如果有两个序列,如果一个序列中与上一个序列对比，少了一个，则只计算到最短的那个序列值
list_y = [1,2,3,4]
r3 = map(lambda x,y:x+y, list_x, list_y)
print(list(r3))