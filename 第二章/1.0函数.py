# 定义带参数函数
def print_line(char, length):
    print(char * length)

# 调用函数，传入参数
print_line('-', 30)
print_line('=', 20)



# 定义：计算矩形面积，接收长l和宽w两个形参
def rectangle_area(l, w):
    return l * w  # return 关键字返回计算结果

# 调用：传入实参20和10，将返回值赋值给变量r_area
r_area = rectangle_area(20, 10)
print(r_area)  # 输出：200


def circle_area_len(r):
    # 同时返回圆的面积和周长，自动封装为元组
    return 3.14 * r * r, 2 * 3.14 * r

al = circle_area_len(10)
print(al)  # 输出：(314.0, 62.800000000000004)


def circle_area_len(r):
    return 3.14 * r * r, 2 * 3.14 * r

# 用两个变量分别接收元组中的两个返回值
area, length = circle_area_len(10)
print(area, length)  # 输出：314.0 62.800000000000004