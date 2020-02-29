'''
1. 如果函数需要传参数怎么办,还不止一个，这时候需要改变装饰器 *args
'''

import time


def decorator(func):
    def wrapper(*args):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        func(*args)
    return wrapper

@decorator
def f1(func_name):
    print('this is f1 function' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('this is f2 function' + func_name1)
    print('this is f3 function' + func_name2)

f1('a')
f2('a','b')