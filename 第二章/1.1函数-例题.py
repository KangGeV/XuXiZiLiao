# 1.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。
# 2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)。
# 3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数),并返回。


# def triangle(d,h):
#     """
# 根据底和高计算三角形的面积
#     :param d: 三角形的低
#     :param h: 三角形的高
#     :return: 三角形的面积
#     """
#     area = d * h /2
#     return area
# D = float(input("请输入三角形的底:"))
# H = float(input("请输入三角形的高:"))
# S = triangle(D,H)
# print(S)

# # 2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)。
# def count(s):
#     """
#     计算传入的字符串中元音字母的个数
#     :param s: 输入的串字符
#     :return: 串字符个数
#     """
#     num = 0
#     for x in s:
#         if x in "aeiouAEIOU":
#             num += 1
#     return num
#
# A = input("请输入串字符:")
# print(count(A))




def calculate_stats(scores):
    """
    计算成绩列表的最高分、最低分、平均分
    :param scores: 成绩列表（数字）
    :return: 最高分, 最低分, 平均分（保留1位小数）
    """
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    # 保留1位小数
    avg_score = round(avg_score, 1)
    return max_score, min_score, avg_score

# 输入处理：假设成绩用逗号分隔，如 "85,92,78"
input_str = input("请输入成绩列表（用逗号分隔，例如 85,92,78）: ")
# 将字符串分割成列表，并转换为浮点数
score_list = [float(x.strip()) for x in input_str.split(",")]

result = calculate_stats(score_list)
print(f"最高分: {result[0]}, 最低分: {result[1]}, 平均分: {result[2]}")








