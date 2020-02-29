'''
1. 继承
'''

from res.code import Student
class Print(Student):
    
    def __init__(self, name, category):
        self.category = category
        # 调用父类的构造函数
        # Student.__init__(self, name)
        # 用super 关键字,子类Print 继承父类Student
        super(Print, self).__init__(name)

    def print_category(self):
        # 调用父类方法
        Student.do_homework(self)
        print(self.name + "正在写" + self.category)

    def do_homework(self):
        # 子类也可以调用父类的方法
        # 如果与父类重名的话，子类只会调用自身的方法
        # 如果还需要调用父类的方法
        super(Print, self).do_homework()
        print("this is child methods")


print1 = Print('John', 'Chinese')
print1.print_category()
print1.do_homework()