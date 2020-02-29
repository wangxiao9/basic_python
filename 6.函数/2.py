'''
1. 函数
 - 解决代码重复利用
 - def 定义函数
    - def funcname():
    - ()可以传参数，也可以不传
 - return 返回函数里的值
'''

'''
2. 定义一个相加的函数
'''

def add_methods(x,y):
    return x + y

# 函数调用 add() 传了两个参数，所以我们也需要传值，不传会报错
# add_methods() 错误的调用方式
# 1 对应的 x ,2 对应 y
print(add_methods(1,2))
# 如果想把2写在前面，可以直接指派
print(add_methods(y=2, x=1))

'''
3. 函数不能同名,但是我们定义的时候运行不会报错，后一个会覆盖前一个
'''
def fun():
    print("fun")

def fun():
    print("fun2")

fun()