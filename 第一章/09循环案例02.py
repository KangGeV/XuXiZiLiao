# #一.例题:猜数字
#
# #生产随机数代码
# # import random
# # random_num=random.randint(1,100)
#
# import random
# A = random.randint(1,100)
#
# while True:#不限制次数,可以用while True
#
#     #比较大小
#     numb = int(input("请输入数字:"))
#     if numb > A:
#         print("猜大了")
#     elif numb < A:
#         print("猜小了")
#     elif numb == A:
#         print("猜对了")
#         break

#二 1.需求1:将1-1000之间(含1000)所有的5的倍数的数字累加起来。

# i = 0
# for j in range(0,1001,5):#注意必须写到1001,前包含后不包含
#     i += j
# print(i)


# #二 2.统计字符串"akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"字符串中有多少个a和k。
# A = input("请输入字符串")#注意输入是input,不能写成print
# i = 0
# j = 0
# for b in A:#不能用range(),因为A是字符串集合,所有直接引用
#     if b=="a":
#         i = i+1
#     elif b=="k":
#         j = j+1
#
# print(f"其中a有{i}个,k有{j}个")

