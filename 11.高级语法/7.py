'''
1. filter
 - 接收一个函数或者none, 一个序列
'''
list_x = [1,2,3,4,5,6,7,8,9,10]
r = filter(lambda x : x%2==0, list_x)

# 筛选出偶数序列
print(list(r))