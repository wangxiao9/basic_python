'''
1. 变量
 - 类变量
 - 实例变量
'''

# 类变量，顾名思义类里面的变量，可以直接用(类.变量名)访问，函数中要是想访问类变量必须是(类.变量名)，直接访问变量名是不对的
class Student():
    name = 'wangxiao'
    age = '18'

    # 实例变量，这里定义的do_homework中name就是实例变量，name 为do_homework方法中独有的
    def do_homework(self, name):
        print(name + "do homework")

    # def print(self):
    #     print(name)
    
    def print(self):
        print(Student.name)
        # 内置函数__class__ 访问类变量
        print(self.__class__.name)

student1 = Student()
student1.do_homework('jodie')
print(Student.name)
student1.print()