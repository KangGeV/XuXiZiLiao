mue = """
#   #   #   #   #   #   #   #   #   #    菜单   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

#   1.添加学生信息    2.修改学生信息    3.删除学生信息    4.查询学生信息    5.列出所有学生    6.统计班级成绩    7.退出系统  #
 
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #  """

dict_student = {"name":{"语文:":90.0,"数学:":92.0,"英语:":93.0}}

print(mue)



while True:
    A = int(input("请输入需要执行的操作(1-7)"))
    match A:
            case 1:
                name_student = input("请输入学生姓名:")
                if name_student  in dict_student:
                    print("该学生已录入,请选择其他操作!")
                    continue

                A = float(input("请输入语文成绩:"))
                B = float(input("请输入数学成绩:"))
                C = float(input("请输入英语成绩:"))
                dict_student[name_student] = {"语文:": A,"数学:": B,"英语:": C}

            case 2:
                name_student = input("请输入学生姓名:")
                if name_student not in dict_student:
                    print("该学生未已录入,请选择其他操作!")
                    continue

                A = float(input("请输入语文成绩:"))
                B = float(input("请输入数学成绩:"))
                C = float(input("请输入英语成绩:"))
                dict_student[name_student] = {"语文:": A, "数学:": B, "英语:": C}
            case 3:
                name_student = input("请输入学生姓名:")
                if name_student not in dict_student:
                    print("该学生未已录入,请选择其他操作!")
                    continue

                del dict_student[name_student]
            case 4:
                name_student = input("请输入学生姓名:")
                if name_student not in dict_student:
                    print("该学生未已录入,请选择其他操作!")
                    continue

                dict_student.get(name_student)
            case 5:
                dict_student.values()
            case 6:#统计班级成绩,统计班级语文,数学,英语的最高分,最低分,平均分,语文,数学,英语最高分和最低分的同学.
                chinese = [s["语文:"] for s in dict_student.values()]#语文成绩集合
                match = [s["数学:"] for s in dict_student.values()]#数学成绩集合
                english = [s["英语:"] for s in dict_student.values()]#英语成绩集合

                chinese_max = max(chinese)#语文最高分
                chinese_avg = sum(chinese)/len(chinese)#语文平均分
                print(f"语文最高分为:{chinese_max},语文平均分为:{chinese_avg}")

                match_max = max(match)
                match_avg = sum(match) / len(match)
                print(f"数学最高分为:{match_max},数学平均分为:{match_avg}")

                english_max = max(english)
                english_avg = sum(english)/len(english)
                print(f"英语最高分为:{english_max},英语平均分为:{english_avg}")

                chinese.sort()#排序
                print(f"语文最高分为:{chinese[-1]},语文最低分为:{chinese[0]}")
                # print(f"语文最高分的名字为{k for k, v in .items() if v == target}:,语文最低分的名字为:")
                #             # 语文统计
                #             chinese_max = max(chinese_scores)
                #             chinese_min = min(chinese_scores)
                #             chinese_avg = sum(chinese_scores) / len(chinese_scores)
                #             # 找出最高分和最低分的学生姓名
                #             chinese_max_names = [name for name, scores in dict_student.items() if scores["语文:"] == chinese_max]
                #             chinese_min_names = [name for name, scores in dict_student.items() if scores["语文:"] == chinese_min]
                #
                #             print(f"语文最高分: {chinese_max} 分，学生: {', '.join(chinese_max_names)}")
                #             print(f"语文最低分: {chinese_min} 分，学生: {', '.join(chinese_min_names)}")
                #             print(f"语文平均分: {chinese_avg:.2f}")







            case 7:
                print("bye~")
                break
            case _:
                print("操作异常.请重新输入!!!")








# #______________________________________________优化___________________________________________________
# # 初始学生字典（空）
# dict_student = {}
#
# # 菜单（保留原样式）
# mue = """
# #   #   #   #   #   #   #   #   #   #    菜单   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#
# #   1.添加学生信息    2.修改学生信息    3.删除学生信息    4.查询学生信息    5.列出所有学生    6.统计班级成绩    7.退出系统  #
#
# #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #  """
# print(mue)
#
# while True:
#     # 每次循环都接收操作，避免只输入一次
#     choice = input("请输入需要执行的操作(1-7): ")
#
#     match choice:
#         case "1":  # 添加学生信息
#             name = input("请输入学生姓名: ")
#             if name in dict_student:
#                 print("该学生已录入，请选择其他操作!")
#                 continue
#             chinese = float(input("请输入语文成绩: "))
#             math = float(input("请输入数学成绩: "))
#             english = float(input("请输入英语成绩: "))
#             dict_student[name] = {"语文:": chinese, "数学:": math, "英语:": english}
#             print(f"学生 {name} 添加成功！")
#
#         case "2":  # 修改学生信息
#             name = input("请输入学生姓名: ")
#             if name not in dict_student:
#                 print("该学生未录入，请先添加!")
#                 continue
#             chinese = float(input("请输入新的语文成绩: "))
#             math = float(input("请输入新的数学成绩: "))
#             english = float(input("请输入新的英语成绩: "))
#             dict_student[name] = {"语文:": chinese, "数学:": math, "英语:": english}
#             print(f"学生 {name} 信息修改成功！")
#
#         case "3":  # 删除学生信息
#             name = input("请输入学生姓名: ")
#             if name not in dict_student:
#                 print("该学生未录入，无法删除!")
#                 continue
#             del dict_student[name]
#             print(f"学生 {name} 已删除！")
#
#         case "4":  # 查询单个学生信息
#             name = input("请输入学生姓名: ")
#             if name not in dict_student:
#                 print("该学生未录入!")
#                 continue
#             info = dict_student[name]
#             print(f"学生 {name} 的成绩：语文 {info['语文:']}，数学 {info['数学:']}，英语 {info['英语:']}")
#
#         case "5":  # 列出所有学生
#             if not dict_student:
#                 print("暂无学生信息！")
#             else:
#                 print("所有学生信息：")
#                 for name, scores in dict_student.items():
#                     print(f"姓名: {name}, 语文: {scores['语文:']}, 数学: {scores['数学:']}, 英语: {scores['英语:']}")
#
#         case "6":  # 统计班级成绩
#             if not dict_student:
#                 print("暂无学生，无法统计！")
#                 continue
#
#             # 收集各科成绩列表
#             chinese_scores = [scores["语文:"] for scores in dict_student.values()]
#             math_scores = [scores["数学:"] for scores in dict_student.values()]
#             english_scores = [scores["英语:"] for scores in dict_student.values()]
#
#             # 语文统计
#             chinese_max = max(chinese_scores)
#             chinese_min = min(chinese_scores)
#             chinese_avg = sum(chinese_scores) / len(chinese_scores)
#             # 找出最高分和最低分的学生姓名
#             chinese_max_names = [name for name, scores in dict_student.items() if scores["语文:"] == chinese_max]
#             chinese_min_names = [name for name, scores in dict_student.items() if scores["语文:"] == chinese_min]
#
#             print(f"语文最高分: {chinese_max} 分，学生: {', '.join(chinese_max_names)}")
#             print(f"语文最低分: {chinese_min} 分，学生: {', '.join(chinese_min_names)}")
#             print(f"语文平均分: {chinese_avg:.2f}")
#
#             # 数学统计
#             math_max = max(math_scores)
#             math_min = min(math_scores)
#             math_avg = sum(math_scores) / len(math_scores)
#             math_max_names = [name for name, scores in dict_student.items() if scores["数学:"] == math_max]
#             math_min_names = [name for name, scores in dict_student.items() if scores["数学:"] == math_min]
#
#             print(f"数学最高分: {math_max} 分，学生: {', '.join(math_max_names)}")
#             print(f"数学最低分: {math_min} 分，学生: {', '.join(math_min_names)}")
#             print(f"数学平均分: {math_avg:.2f}")
#
#             # 英语统计
#             english_max = max(english_scores)
#             english_min = min(english_scores)
#             english_avg = sum(english_scores) / len(english_scores)
#             english_max_names = [name for name, scores in dict_student.items() if scores["英语:"] == english_max]
#             english_min_names = [name for name, scores in dict_student.items() if scores["英语:"] == english_min]
#
#             print(f"英语最高分: {english_max} 分，学生: {', '.join(english_max_names)}")
#             print(f"英语最低分: {english_min} 分，学生: {', '.join(english_min_names)}")
#             print(f"英语平均分: {english_avg:.2f}")
#
#         case "7":
#             print("bye~")
#             break
#
#         case _:
#             print("操作异常，请重新输入(1-7)!")