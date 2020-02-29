'''
1. 静态方法
'''

class Student():
    name = 'wangxiao'
    age = '18'
    num = 0

    def do_homework(self, name):
        print(name + " do homework")
 
    @classmethod
    def plus(cls):
        cls.num += 1
        print("当前总是为：" + str(cls.num))

    # 静态方式，不需要实例参数
    # 需要添加装饰器@staticmethod
    # 静态方法是独立的，可以理解成与类没有特别的关联
    @staticmethod
    def add(x, y):
        print("this is staticmethod")

    
student1 = Student()

# 类和实例都可以调用
student1.add(1, 3)
Student.add(1, 2)