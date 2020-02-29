'''
ep: sum = 0 , 每次相加后不归为0 要求在此基础上增加
'''

# 非闭包方式
sum = 0 
def add(x):
    global sum
    new_sum = sum + x
    sum = new_sum
    return sum

print(add(1))
print(add(2))
print(add(3))

# 闭包方式
def count(origin):
    def add(x):
        nonlocal origin
        new_sum = origin + x
        origin = new_sum
        return origin
    return add

s = count(0)
print(s(1))
print(s(2))
print(s(3))



