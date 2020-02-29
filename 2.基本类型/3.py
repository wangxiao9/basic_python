# 字符串运算
a = 'hello'
b = 'world'
c = a + b
print("加法:" + c)

'''
1. 字符串之间是不可以相乘的
   print("乘法" + a*b)
2. 单个字符串是可以相乘的
'''
print("乘法" + a*2)

# 访问字符串中某一个字母
print(len(c))
# 得到第一个字符，下标从0开始
print("获取字符串第一个字母:" + c[0])
print("获取字符串第4个字母:" + c[4])

'''
# 如果超出字符的长度，报错IndexError: string index out of range，超出了界限
print(c[10])
'''

# 负数从最后往前开始计算
print("获取字符串最后一个字母:" + c[-1])
# 截取一组字符
print("截取一段字母:" + c[2:4])
# -1 往末尾往前开始数
print(c[2:-1])
# 如果超过边界值则一直获取到最后的数值
print("超出字符长度:" + c[2:10])
print("超出字符长度:" + c[2:11])
print("截取从第二个字符到最后:" + c[2:])

'''
ep1: 字符串 "java python c# php js" 截取java 到 php的字符串
'''
language = "java python c# php js"
print("ep1:" + language[:-2])

'''
ep2: 字符串 "java python c# php js" 截取python 到 js的字符串
'''
print("ep2:" + language[5:])

'''
ep3: 字符串 "java python c# php js" 截取js的字符串
分析上面的例子比较好理解，如果字符过长的话，一个个数会比较麻烦
'''
print("ep3:" + language[-2:])

