# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下
# 1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩质、英语成绩，记录在系统中
# 1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
# 1.2 检查学生姓名是否已存在，如果学生不存在，再添加 (存在则，不添加)
# 1.3 验证成绩范围 (0-100 分)
# 1.4 创建学生对象并添加到系统

# 2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
# 2.1 输入要修改的学生姓名
# 2.2 根据姓名查找该学生，显示该生当前成绩信息
# 2.3 输入新的语文、数学、英语成绩
# 2.4 更新学生成绩数据

# 3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩

# 4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
# 4.1 输出格式为:"姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"

# 5. 展示全部学生成绩：展示出系统中所有学生的成绩

class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名:{self.name}| 语文{self.chinese} | 数学{self.math} | 英语{self.english} | 总分:{self.chinese + self.english + self.math}"

    def update_score(self,chinese = None,math = None,english = None):
        if chinese is not None :
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

#添加学生成绩
    def add_student(self):
        name = input("请输入添加学生的姓名")
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在,添加失败!")
                return

        chinese = int(input("请输入学生的语文成绩"))
        math = int(input("请输入学生的数学成绩"))
        english = int(input("请输入学生的英语成绩"))

        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)



    #修改学生成绩
    def update_student(self):
        name = input("请输入需要修改的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"该学生的成绩为:{s}")

                chinese = int(input("请输入修改后的语文成绩"))
                math = int(input("请输入修改后的数学成绩"))
                english = int(input("请输入修改后的英语成绩"))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功~")
                    print(f"修改后的成绩为:{s}")
                    return

                else:
                    print("修改的成绩必须在0-100之间")
                    return

        print("未找到该学生,修改失败!")

#删除学生成绩
    def delete_student(self):
        name = input("请输入需要删除的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                return
        print("未找到该学生,删除失败!")

#查询学生成绩
    def query_student(self):
        name = input("请输入需要查询的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"该学生的成绩为:{s}")
                return
        print("未找到该学生,查询失败!")
#展示学生成绩
    def show_student(self):
        for s in self.student_list:
            print(s)


#运行系统的方式
    def run(self):
        print(f"欢迎使用教务系统V{EduManagement.system_version}")
        while True:
            print()
            print("#    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    ")
            print("#    #     1.添加学生     2.修改学生      3.删除学生      4.查询学生      5.展示学生     6.退出系统    #    ")
            print("#    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    ")

            choice = input("请选择要执行的操作(1-6):")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.show_student()
                case "6":
                    print("bye~~")
                    break
                case _:
                    print("输入错误,请选择1-6之前的菜单功能!")

if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()

















#测试
if __name__ == '__main__':
    s1 = Student("王林",90 ,60,70)
    print(s1)
