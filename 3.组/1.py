'''
1. 认识列表list
    - 列表可变
    - 列表用[] 括起来
    - 访问里面内容用list[0]
'''
a = [1,2,3,4,5,6,7,8,9,10]
print(type(a))  # <class 'list'>

# 列表中不仅可以存相同类型，可以存不同类型
b = [1,2,'hello',True,'world']
print(type(b)) # <class 'list'>

'''
2. 列表的操作
 总结： 一个列表截取，还是列表
'''
# ep1: 获取列表a中的5
print("ep1:" , a[4])
# ep2: 获取 3-5
print('ep2:' , a[2:4])
# ep3: 获取列表b中的hello,True
print('ep3:', b[2:4])
# ep4: 改变b中，把2改成字符串’Second‘
b[1] = 'Second'
print('ep4:', b)
# ep5: b列表中，复制一个相同的列表
print('ep5:', b * 2)
# ep6: 往a列表中增加一个布尔值False
a.append(False)
print('ep6:', a)
# ep7: a列表中删除8
a.remove(8)
print('ep7:', a)
# ep8: a列表中删除3，用pop, 注意pop() 是下标
a.pop(2)
print('ep7:', a)

