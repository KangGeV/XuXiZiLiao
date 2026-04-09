# 1.定义一个函数,根据传入的分数,计算对应的分数等级并返回。
# 分数>=90:A
# 分数>=75:B
# 分数>=60:C
# 分数<60:D
# 2.定义一个函数,用于判断一个字符串是否是回文串,返回bool值。
# 把字符串反转,如果和原字符串相同,就是回文串。(如:"level","radar","黄山落叶松叶落山黄")
# 3.定义一个函数:完成时间转换功能,将传入的秒转换为小时、分钟、秒。
# 4.定义一个函数:根据传入的三角形三个边的边长,判定三角形的类型(等边、等腰、普通,或者不能构成三角形)。
from asyncio import run_coroutine_threadsafe
from operator import truediv


# 1.定义一个函数,根据传入的分数,计算对应的分数等级并返回。
# 分数>=90:A
# 分数>=75:B
# 分数>=60:C
# 分数<60:D
#
# def get_grade(score):
#     """根据分数返回等级"""
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
#
# # 输入分数并调用函数
# score = float(input("请输入成绩分数: "))
# grade = get_grade(score)
# print(f"分数 {score} 对应的等级是: {grade}")


# 2.定义一个函数,用于判断一个字符串是否是回文串,返回bool值。
# 把字符串反转,如果和原字符串相同,就是回文串。(如:"level","radar","黄山落叶松叶落山黄")
#
# def is_palindrome(s):
#     """判断字符串是否为回文串"""
#     reversed_s = s[::-1]
#     return s == reversed_s   # 直接返回比较结果
#
# # 测试
# test_str = input("请输入一个字符串: ")
# result = is_palindrome(test_str)
# print(f"是否是回文: {result}")





# # 3.定义一个函数:完成时间转换功能,将传入的秒转换为小时、分钟、秒。
#
# def miao(s):
#
#     h = int((s/(60*60))%60) #小时
#     f = int(((s-(60*60)*h)/60)%60)#分钟
#     m = (s-(60*60)*h)-f*60#秒钟
#     return h,f,m
#
# A = int(input("请输入秒钟"))
# print(miao(A))
#
#
# # ---------------------------------------优化----------------------------------------------------------
# def convert_seconds(total_seconds):
#     """
#     将秒转换为小时、分钟、秒
#     :param total_seconds: 总秒数（整数）
#     :return: (小时, 分钟, 秒)
#     """
#     hours = total_seconds // 3600          # 整除得到小时
#     remainder = total_seconds % 3600       # 剩余秒数（不足一小时的部分）
#     minutes = remainder // 60              # 整除得到分钟
#     seconds = remainder % 60               # 取余得到秒
#     return hours, minutes, seconds
#
# # 测试
# seconds = int(input("请输入秒数: "))
# h, m, s = convert_seconds(seconds)



# 4.定义一个函数:根据传入的三角形三个边的边长,判定三角形的类型(等边、等腰、普通,或者不能构成三角形)。