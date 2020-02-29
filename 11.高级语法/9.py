'''
1. 装饰器方法解决
 - 装饰器用@ 语法
'''
import time


def decorator(func):
    def wrapper():
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        func()
    return wrapper

@decorator
def f1():
    print('this is f1 function')

@decorator
def f2():
    print('this is f2 function')


f1()
f2()