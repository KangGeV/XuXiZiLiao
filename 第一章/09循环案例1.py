#计算1-100 所有奇数的和

j = 0
for i in range(1,100):
    if i % 2 == 1:
        j = j + i
print(f"{j}")


#简化

# j = 0
# for i in range(1,101,2):
#     j = j + i
# print(f"{j}")




            #打印一个长度为6,宽为4的 # 长方形

#   #   #   #   #   #
#   #   #   #   #   #
#   #   #   #   #   #
#   #   #   #   #   #

#print("#")自带换行效果,每次执行都会输出新的一行
# print("#",end=""):end输入表示每次输出以什么结束;默认是"\n",表示换行

# 1 .接受输入的长和宽
m = int(input("请输入长方形的长:"))
n = int(input("请输入长方形的宽:"))
# Shift + Enter 可以快速换行

# 2 .打印 # 矩阵
for i in range(0,n+1):      #输出列
    for j in range(0,m+1):  #输出行
        print("#",end=" ")  #end""取消换行
    print()                 #print()默认换行,注意缩进,与for顶齐



        # # 打印 9*9 乘法表
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end="\t")
#     print()





