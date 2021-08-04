"""
----------------------------------------
    File Name: chush
    Author: Kong
    Date: 2021/7/19
    Description: 
----------------------------------------
"""
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')

    def __repr__(self):
        return f'{self.name}: {self.age}'
stu1 = Student('kong', 20)
print(stu1)
stu2 = Student('王大锤', 15)
stu1.study('Python程序设计')    # kong正在学习Python程序设计.
stu2.play()                    # 王大锤正在玩游戏
students = [stu1, Student('王小锤', 16), Student('王大锤', 25)]
print(students)    # [kong: 20, 王小锤: 16, 王大锤: 25]