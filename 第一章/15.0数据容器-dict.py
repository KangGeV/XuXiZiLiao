# 1. 定义字典
dict1 = {"王林": 670, "李慕婉": 608, "徐立国": 580, "韩立": 688}
dict2 = {0: 670, 1.5: 608, (1, 2): 580, ('A', 'B'): 688}

# 2. 查看字典与类型
print("dict1:", dict1)
print("dict1的类型:", type(dict1))
print("dict2:", dict2)

# 3. 访问与修改
print("李慕婉的分数:", dict1["李慕婉"])
dict1["李慕婉"] = 688  # 修改值
print("修改后dict1:", dict1)

# 4. 重复key示例
dict3 = {"a": 1, "a": 2}
print("重复key的字典:", dict3)  # 输出 {'a': 2}



