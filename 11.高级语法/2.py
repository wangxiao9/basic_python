'''
1. 闭包
 - 闭包组成 = 函数 + 局部环境变量
'''

'''
2. 闭包的正确演示，闭包的意思是，当函数Animal 内部返回了do的函数，并且还使用了局部变量animal用于被返回的do函数
'''
def Animal():
    animal = 'dog'
    def do():
        print(animal + "is people's friend")
    return do

a = Animal()
# 说明a是一个闭包，由环境变量+函数组成，并且要把这个函数给返回出去
print(a.__closure__)  # (<cell at 0x10ea4f108: str object at 0x10ea7e730>,)
print(type(a))

# 错误的演示, 不能直接调用内部的函数
# a = do() NameError: name 'do' is not defined

'''
3. 闭包内函数不受外部的变量影响
'''
sum = 10

def Sum():
    sum = 0
    def add(x, y):
        count = sum + x + y
        return count
    return add

f = Sum()
print(f(2,3))  # 计算结果是5， 变量的作用域只在函数内部，不受全局变量控制

'''
4. 如果没有局部环境变量就不是一个闭包
'''

def people():
    def do():
        print("人类在毁灭地球")
    return do

f = people()
print(f.__closure__) # None, 说明这不是一个闭包

