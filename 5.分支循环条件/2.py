'''
1. 循环
 - for in , while
'''

'''
2. for 循环
'''

'''
ep1:
求1+2+3+...+100 值
'''
sum = 0
for x in range(1,101):
    sum += x
print('ep1 =', sum)

'''
range(1,100) : 生成1-99的整数序列
range(1,100,2): 生成1-99的基数数列，从1开始
'''

'''
ep2:
求1+3+...+99 值
'''
sum = 0
for x in range(1,100,2):
    sum +=x
print('ep2 =', sum)

# 用分支来实现求偶数和
sum = 0
for x in range(1,100):
    if x % 2 == 0:
        sum +=x
print('ep2 =', sum)

'''
ep3:打印下面的图形
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *      *  *  1
   ***     *  *  (2+1)
  *****    *  *  (3+2)
 *******
*********

'''
# row = int(input("row ="))
for i in range(1,6):
    for j in range(i,i+1):
        print("*"*j)
print("------------------")
for i in range(1,6):
    for j in range(i,i+1):
        print(" "*(6-1-i)+"*"*i)
print("------------------")
for i in range(1,6):
    for j in range(i,i+1):
        print(" "*(6-1-i)+"*"*i+"*"*(j-1))

'''
3. while 
 - 如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。
'''
count = 0
while True:
    count += 1
    if count < 1:
        continue
    if count > 10:
        break

print(count)