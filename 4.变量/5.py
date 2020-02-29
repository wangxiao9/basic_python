'''
运算符
 - 逻辑运算符
 - and or not
 - float 0被认为是False 非0为True
 - 对于str字符串，空字符串为False,其他为True
 - 列表,元组,字典, 空字符串为False,其他为True
'''

a = 1
b = 2

True and False
True or False
not True
# ep1: and(且),1 and 2 ,1,2都是真,为什么返回的事2，因为先读取了1，后面又继续读取了2，计算机返回了后面一个
print('ep1:', a and b) #2
print('ep1:', b and a) #1

# ep2: or 或 读取第一个为真，就不在读后面一个
print('ep2:', a or b)  #1
print('ep2:', b or a)  #1
# ep3: not 
print('ep3:', not True)