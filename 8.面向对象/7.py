'''
1. 成员的可见性
'''

class Student():
    name = 'wangxiao'
    # 私有属性
    # __private_attr 用下划线__ 表示私有属性
    __age = '18'
    num = 0

    def __init__(self, name):
        self.name = name

    def do_homework(self):
        print(self.name + " do homework")

    def marking_student(self):
        print("学生的姓名是:" , self.name)
        # 私有方法可以被内部调用，但是不可以被外部调用，不允许更改
        self.__marking_age()

    # 私有方法
    # __private_method 用下划线__ 表示私有方法
    def __marking_age(self):
        print("学生的年龄是:" , self.__age)

    @classmethod
    def plus(cls):
        cls.num += 1
        print("当前总是为：" + str(cls.num))

    @staticmethod
    def add(x, y):
        print("this is staticmethod")

student1 = Student('jack')
student1.do_homework()
# AttributeError: type object 'Student' has no attribute '__age'
# 类无法直接访问私有属性
# print(Student.__age)

student1.marking_student()

# 应用场景: 如果你不想被外部更改，使用，可以定义一个私有方法