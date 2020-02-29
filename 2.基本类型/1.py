'''
type() 检查变量类型
'''
# 数字类型
# 整型
type(1)
type(2//2) # 取整

# 浮点型
type(1.0)
type(1+1.0)
type(2/2) # 整除

# 布尔类型
type(True)
type(False)
'''
数字0 -> False
数字1 -> True
'''
bool(0) == False
bool(1) == True

# 字符串类型
type('hello world')
type("hello world")

# 对变量进行转换
int() # 转换成整型
float() # 转化成浮点型
str() # 转化成字符串型
ord() # 将字符串（一个字符）转换成对应的编码（整数）。