'''
1. 如果函数需要传关键字 
 - 关键字用**kw
'''

import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        func(*args, **kw)
    return wrapper

@decorator
def f1(func_name):
    print('this is f1 function' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('this is f2 function' + func_name1)
    print('this is f3 function' + func_name2)

@decorator
def f3(**kw):
    print(kw)

f1('a')
f2('a','b')
f3(a=1,b=2)
