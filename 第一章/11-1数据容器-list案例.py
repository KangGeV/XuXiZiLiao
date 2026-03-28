#案例1.将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值、最大值和平均值

# 定义列表
j = 1
my_list = []

#将输入的数据存入列表
for i in range(1,11):
    s = int(input(f"请输入第{j}个数"))
    my_list.append(s)
    j += 1

#输出列表
print(my_list)

#排序
my_list.sort()
print("排序后的数字为:",my_list)

# 输出最大值和最小值
print(f"最大值为:",my_list[0])
print(f"最小值为:",my_list[-1])

# 平均值  sum()为求和函数,len为数据容器长度
print("平均值:",sum(my_list)/len(my_list))

