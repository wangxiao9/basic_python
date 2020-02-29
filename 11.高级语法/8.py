'''
1. 装饰器
'''
import time

# 普通方法解决
def f1():
    print('this is f1 function')

def f2():
    print('this is f2 function')

# 当前有两个函数，需求，现在要调用时间函数，再不修改f1,f2函数的基础上，新增一个时间函数
def print_time():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print_time()
f1()
print_time()
f2()
