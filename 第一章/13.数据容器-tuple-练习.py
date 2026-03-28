# 元组基本操作
t1 = (80, 95, 78, 50, 76, 80, 85, 20)
print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1])

# 切片
print(t1[0:5:1])

# 统计元素个数
print(t1.count(80))

# 获取元素索引
print(t1.index(80))

# 空元组
t2 = ()
print(t2)
print(type(t2))

# 单元素元组
t3 = (100,)
print(t3)
print(type(t3))




# 组包
t1 = (5, 7, 9, 1)
t2 = 5, 7, 9, 1  # 隐式组包，等价于元组

# 基础解包
a, b, c, d = t1
print("基础解包:", a, b, c, d)  # 输出: 5 7 9 1

# 扩展解包
x, *y, z = t2
print("扩展解包1:", x, y, z)  # 输出: 5 [7, 9] 1

s, *o = t2
print("扩展解包2:", s, o)  # 输出: 5 [7, 9, 1]

*o, e = t2
print("扩展解包3:", o, e)  # 输出: [5, 7, 9] 1



# 初始变量
a = 10
b = 20

# 交换变量（组包+解包一步完成）
a, b = b, a

# 输出结果
print("交换后 a =", a)  # 输出：交换后 a = 20
print("交换后 b =", b)  # 输出：交换后 b = 10