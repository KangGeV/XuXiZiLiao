# # #案例2:合并两个列表中的元素,并对合并的结果进行去重处理(去除列表中的重复元素)
# #
# # # 定义两个列表
# # num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# # num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# #
# # # 方法1：+ 运算符合并
# # num_list_add = num_list1 + num_list2
# # print("+ 运算符合并结果：", num_list_add)
# #
# # # 方法2：* 解包合并
# # num_list_unpack = [*num_list1, *num_list2]
# # print("* 解包合并结果：", num_list_unpack)
# #
# # # 判断元素存在 + 去重示例
# # new_list = []
# # for num in num_list_add:
# #     if num not in new_list:
# #         new_list.append(num)
# # print("去重后列表：", new_list)
# #
# # # 单独判断示例
# # print("54 是否存在于 num_list1：", 54 in num_list1)
# # print("100 是否存在于 num_list2：", 100 in num_list2)
#
# #
# # # 1.生成1-20的平方列表。
# # # 2.从如下数字列表中提取所有偶数,并计算其平方,组成一个新的列表。
# #
# # # 1.定义数据容器
# # A = []
# #
# # # 2.计算1-20的平方
# # for i in range(1,21):
# #     j = i**2
# #     i += 1
# #     A.append(j)
# # # 3.输出数据集
# # print(A)
# #
# # # 4.筛选其中的偶数
# # B = []
# # for c in A:
# #     if c % 2 == 0:
# #         B.append(c)
# # print(B)
#
# #
# # # 1.生成1-20的平方列表。
# # # 2.从如下数字列表中提取所有偶数,并计算其平方,组成一个新的列表。
# #
# # # 1.定义数据容器
# # A = []
# #
# # # 2.计算1-20的平方
# # for i in range(1,21):
# #     A.append(i**2)
# #
# # # 3.输出数据集
# # print(A)
# #
# # # 4.筛选其中的偶数
# # B = []
# # for c in A:
# #     if c % 2 == 0:
# # #         B.append(c)
# # # print(B)
# #
# # # 1.生成1-20的平方列表。
# # # 2.从如下数字列表中提取所有偶数,并计算其平方,组成一个新的列表。
# # # 列表推导式:就是按照一定的规则快速生产一个列表的方式
# # # 推导式1:[要插入的值 for i in 集合/序列]
# # # 推导式2:
# #
# # # 1.计算1-20的平方
# # num_list1 = [i**2 for i in range(1, 21)]
# # # 2.筛选其中的偶数
# # num_list2 = [j for j in num_list1 if j%2==0]
# #
# # print(num_list1)
# # print(num_list2)
# from plistlib import InvalidFileException
#
# # 原始列表
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
# # 1. 合并三个列表
# merged = list1 + list2 + list3
# print("合并后的列表:", merged)
#
# # 2. 去重（使用循环判断）
# unique = []
# for item in merged:
#     if item not in unique:
#         unique.append(item)
# print("去重后的列表:", unique)
#
# # 3. 排序
# unique.sort()
# print("排序后的列表:", unique)


# #将如下列表中能被3或5整除的元素提出来,并获取这些数字对应的平方,组成一个新的列表。
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15,16,17,18,19,20,21,22,22, 23, 24,
# 25,26,27,28,29,30]
#
# #能被3整除的元素对应的平方
# list2 = [i**2 for i in list1 if i%3 == 0 or i%5 == 0 ]
# print("能被3或5整除的元素对应的平方",list2)





# #将如下列表中的正数提取出来,封装为一个新的列表。
# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11,16, 54, -14, 36, -16, 87, -39]
#
# list2 = [i for i in list1 if i > 0]
# print("其中的正数为",list2)



