# 学号	    姓名	语文	数学	英语
# 2026001	陈宇	88	95	92
# 2026002	林晓	76	82	78
# 2026003	王梓	90	89	91
# 2026004	李悦	85	79	84
# 2026005	张恒	92	96	87
# 2026006	刘琪	79	85	80
# 2026007	黄俊	83	91	77
# 2026008	周雅	94	88	95
# 2026009	吴浩	72	75	73
# 2026010	郑欣	86	84	89

# 根据提供的学生成绩单,完成如下需求:
# 1.计算每个学生的总分、各科平均分,然后一并输出出来。
# 2.统计各科成绩的最低分、最高分、平均分,并输出。
# 3.查找成绩优秀(平均分大于90)的学生,并输出。

# 10 名学生信息：(学号, 姓名, 语文, 数学, 英语)
students = (
    ("2026001", "陈宇", 88, 95, 92),
    ("2026002", "林晓", 76, 82, 78),
    ("2026003", "王梓", 90, 89, 91),
    ("2026004", "李悦", 85, 79, 84),
    ("2026005", "张恒", 92, 96, 87),
    ("2026006", "刘琪", 79, 85, 80),
    ("2026007", "黄俊", 83, 91, 77),
    ("2026008", "周雅", 94, 88, 95),
    ("2026009", "吴浩", 72, 75, 73),
    ("2026010", "郑欣", 86, 84, 89)
)
# 1.计算每个学生的总分、各科平均分,然后一并输出出来。

for s in students:
    total =  +s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]}\t{s[1]}的总分为:{total},平均成绩为:{avg:.1f}")

# 2.统计各科成绩的最低分、最高分、平均分,并输出。
Chinese = [s[2] for s in students]
mint = [s[3] for s in students]
English = [s[4] for s in students]
print(f"语文的最高成绩为:{max(Chinese)},最低分为:{min(Chinese)},平均分为:{sum(Chinese)/len(Chinese)}")


# 3.查找成绩优秀(平均分大于90)的学生,并输出。

for s in students:
    total =  +s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
        print(f"{s[0]}\t{s[1]}的成绩为优秀")






# # 学生数据
# students = (
#     ("2026001", "陈宇", 88, 95, 92),
#     ("2026002", "林晓", 76, 82, 78),
#     ("2026003", "王梓", 90, 89, 91),
#     ("2026004", "李悦", 85, 79, 84),
#     ("2026005", "张恒", 92, 96, 87),
#     ("2026006", "刘琪", 79, 85, 80),
#     ("2026007", "黄俊", 83, 91, 77),
#     ("2026008", "周雅", 94, 88, 95),
#     ("2026009", "吴浩", 72, 75, 73),
#     ("2026010", "郑欣", 86, 84, 89)
# )
#
# # 1. 每个学生的总分、平均分
# print("=== 学生成绩统计 ===")
# for stu in students:
#     stu_id, name, chn, math, eng = stu
#     total = chn + math + eng
#     avg = total / 3
#     print(f"{stu_id}\t{name}\t总分:{total}\t平均分:{avg:.1f}")
#
# # 2. 各科成绩的最低分、最高分、平均分
# # 提取各科分数列表
# chinese_scores = [s[2] for s in students]
# math_scores = [s[3] for s in students]
# english_scores = [s[4] for s in students]
#
# print("\n=== 各科统计 ===")
# # 语文
# print(f"语文 - 最高分:{max(chinese_scores)}, 最低分:{min(chinese_scores)}, 平均分:{sum(chinese_scores)/len(chinese_scores):.1f}")
# # 数学
# print(f"数学 - 最高分:{max(math_scores)}, 最低分:{min(math_scores)}, 平均分:{sum(math_scores)/len(math_scores):.1f}")
# # 英语
# print(f"英语 - 最高分:{max(english_scores)}, 最低分:{min(english_scores)}, 平均分:{sum(english_scores)/len(english_scores):.1f}")
#
# # 3. 查找平均分大于90的学生（优秀）
# print("\n=== 优秀学生（平均分 > 90）===")
# for stu in students:
#     stu_id, name, chn, math, eng = stu
#     avg = (chn + math + eng) / 3
#     if avg > 90:
#         print(f"{stu_id}\t{name}\t平均分:{avg:.1f}")