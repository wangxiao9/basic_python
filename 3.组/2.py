'''
1. 认识元组tuple
    - 元组不可变,不可增加不可减少
    - 用() 括起来
'''
a = (1,2,3,True,'hello')
b = (5,6)
print(type(a))
# ep1: 获取列表a中的5
print("ep1:" , a[4])
# ep2: 获取 3-5
print('ep2:' , a[2:4])
# ep3: a+b
print('ep3:' , a + b)