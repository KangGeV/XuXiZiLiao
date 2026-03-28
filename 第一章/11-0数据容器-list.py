
s = ["A","B","C","D","E"]

print(s[0:4:1])

#优化
print(s[:4])



# 1. 创建一个基础列表
my_list = [10, 20, 30, 40, 50]
print("原始列表:", my_list)

# 2. append() 尾部追加单个元素
my_list.append(60)
print("append(60) 后:", my_list)

# 3. insert() 指定索引位置插入元素
my_list.insert(0, 5)   # 索引0插入5
my_list.insert(3, 25)  # 索引3插入25
print("insert 插入后:", my_list)

# 4. remove() 删除第一个匹配的值
my_list.remove(25)
print("remove(25) 后:", my_list)

# 5. pop() 删除并返回元素
# 不写索引：删除最后一个
last_item = my_list.pop()
print("pop() 删除最后一个元素:", last_item)
print("pop() 后列表:", my_list)

# 指定索引：删除对应位置元素
pop_item = my_list.pop(2)
print("pop(2) 删除索引2元素:", pop_item)
print("pop(2) 后列表:", my_list)

# 6. sort() 原地排序
num_list = [5, 2, 9, 1, 5, 6]
num_list.sort()  # 默认升序
print("sort() 升序排序:", num_list)
num_list.sort(reverse=True)  # 降序
print("sort(reverse=True) 降序排序:", num_list)

# 7. reverse() 反转列表
my_list.reverse()
print("reverse() 反转后:", my_list)

# 8. 补充：extend() 追加多个元素
my_list.extend([100, 200, 300])
print("extend([100,200,300]) 后:", my_list)