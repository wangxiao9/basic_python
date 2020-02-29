'''
1. 类方法
 - 如果你想操作有关类想法的操作，建议新建类方法
'''

class Student():
    name = 'wangxiao'
    age = '18'
    num = 0

    def do_homework(self, name):
        print(name + " do homework")

    # 利用self.__class__访问类变量，每次实例化后num + 1
    def addNum(self):
        self.__class__.num +=1
        print("当前总数为：" + str(self.__class__.num))   

    # 利用类方法操作，定义类方法 
    # cls 参数可以换成其他任意参数，self 也可以，python建议cls
    # 注意类方法中要加一个装饰器@classmthod,才表示你是类方法
    @classmethod
    def plus(cls):
        cls.num += 1
        print("当前总是为：" + str(cls.num))


student1 = Student()
student2 = Student()
student3 = Student()

student1.addNum()
student2.addNum()
student3.addNum()

# 类方法，类可以直接调用，不需要进行实例化
Student.plus()
Student.plus()
Student.plus()