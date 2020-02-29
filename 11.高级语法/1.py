'''
1. 枚举
 - emun
 - 枚举不可以被实例化
'''
# 导入枚举类
from enum import Enum, unique

@unique
class Color(Enum):
    YELLOW = '1'
    RED = '2'
    BLACK = '3'
    BLUE = '4'

# 普通的类变量对比
class Color2:
    YELLOW = '1'
    RED = '2'
    BLACK = '3'
    BLUE = '4'

'''
2. 枚举不可以被实例化
'''
# color = Color()
# print(color.BLUE)

print(Color.YELLOW)
print(type(Color.YELLOW))

'''
3. 枚举类中不可以变更常量值
'''
# 枚举类中不可以更改类变量，AttributeError: Cannot reassign members.
# Color.YELLOW = '2' 

# 类变量是可以被修改的
Color2.BLACK = 'black'
print(Color2.BLACK)

'''
4. 获取枚举常量名
'''
print(Color.BLACK.name)

'''
5. 获取枚举常量值
'''
print(Color.BLACK.value)

'''
6. 枚举对比
'''
# 用身份运算符
print(Color.BLACK is Color.BLUE)
print(Color.BLACK is not Color.BLUE)

'''
7. 如果常量内容一致,都指向上一个
'''
print(Color.YELLOW)
print(Color.RED)

# 如果不希望有相同的常量值，可以增加一个装饰器 @unquie
# ValueError: duplicate values found in <enum 'Color'>: RED -> YELLOW

for value in Color.__members__.items():
    print(value)

'''
ep：
'''

class Gender(Enum):
    MALE = 1
    FEMALE = 0

class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


if __name__ == "__main__":
    student = Student('小丽', Gender.FEMALE)
    if student.gender == Gender.FEMALE:
        print(student.name + "is Female")
    else:
        print(student.name + "is Male")