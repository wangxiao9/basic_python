'''
1. 导入
'''

'''
2. ep1: 导入res文件夹下面的code1.py 访问变量a的值
    - 注意导入的模块必须在执行的语句前面，因为python是解释性语言，读取的时候是从上到下
'''

import res.code1
print('ep1:', res.code1.a)

'''
3. ep2: 读取res.code1 太长怎么办
'''

import res.code1 as code
print('ep2:', code.a)

'''
4. ep3: 除了import关键字导入，还有from 模块 import 类 方式
'''
from res import code1
print('ep3:', code1.a)
