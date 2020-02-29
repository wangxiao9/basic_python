class Student():
    name = 'wangxiao'
    __age = '18'
    num = 0

    def __init__(self, name):
        self.name = name

    def do_homework(self):
        print(self.name + " do homework")

    def marking_student(self):
        print("学生的姓名是:" , self.name)
        self.__marking_age()

    def __marking_age(self):
        print("学生的年龄是:" , self.__age)

    @classmethod
    def plus(cls):
        cls.num += 1
        print("当前总是为：" + str(cls.num))

    @staticmethod
    def add(x, y):
        print("this is staticmethod")
