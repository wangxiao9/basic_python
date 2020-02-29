'''
1. 构造函数
'''

class Student():
    name = 'wangxiao'
    age = '18'
    num = 0

    # 构造函数用__init__ 定义
    # 也可以称为初始化
    # 当创建构造函数的时候，实例会先调用这个方法
    # 构造函数是可以被调用的，但是很少有这么使用的
    # 构造函数不能被return
    def __init__(self, name):
        self.name = name

    def do_homework(self):
        print(self.name + " do homework")
        
 
    @classmethod
    def plus(cls):
        cls.num += 1
        print("当前总是为：" + str(cls.num))

    @staticmethod
    def add(x, y):
        print("this is staticmethod")

student1 = Student('jack')
student1.do_homework()

