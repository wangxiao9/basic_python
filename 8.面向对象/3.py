'''
1. 实例方法
'''

class Student():
    name = 'wangxiao'
    age = '18'

    # do_homework 实例方法
    def do_homework(self, name):
        print(name + " do homework")

# 实例方法，可以理解成就是实例化后可用的方法
# 对Student 类实例化
student1 = Student()
# 调用do_homework()方法
student1.do_homework('Jack')