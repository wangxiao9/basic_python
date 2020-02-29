'''
1. 认识字典 dict
 - key:value
 - key不重复
 - key不能修改
 - {} 包裹
'''
a = {'name':'jokie','age':'18'}
print(type(a))

'''
2. 字典的操作
'''
# ep1: 获取name的值
print('ep1:', a['name'])
# ep2: 修改name的值
a['name'] = 'home'
print('ep2:', a)
# ep3: 修改name的值
a['address'] = '江苏'
print('ep3:', a)

'''
3. 空字典显示
'''
{}

'''
4. 字典中可以嵌套字段
'''
b = {1:'1',2:'2',3:{'3':3,'4':4}}
print('b:', type(b))
print('b:', b[3])