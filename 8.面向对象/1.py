'''
1. 面向对象
 - 类 <-> 对象， 我们把类封装起来，做的事
'''

'''
2. 定义一个类
 - 类名建议首字母大写
class Student():
    pass
'''

'''
3. 类中可以用函数实现功能
 - 类中定义的函数，要加一个self 参数 , 但是我们调用的时候不需要传入这个参数，我们实例化类的时候，直接指向这个self
'''
class Student():
    def do_homework(self):
        print('do_homework')
# 实例化
student = Student()
# 调用这个do_homework() 方法
student.do_homework()