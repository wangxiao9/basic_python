'''
运算符
 - 赋值运算符
 - = += -= *= /= %= //= **= &=
'''

a = 'hello'
b = 'world'
c = {1,2,3}
d = {2,3}
# ep1: a+=b 相当于a=a+b
a+=b
print('ep1:', a)
# ep2: 减法运算
c-=d
print('ep2:', c)
