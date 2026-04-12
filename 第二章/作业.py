# 采用面向对象的编程思想,开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据,通过控制台菜单与用户交互。具体功能如下:
from platform import system
from random import choice


# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来,格式为:"商品名称:xxx,商品价格:xxx,商品数量:xxx"。
# 5.退出购物车


# 定义商品类
class Goods:

    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名字：{self.name}| 商品价格：{self.price} |商品数量：{self.num}"

    # 商品的修改工具
    def update_goods(self, price=None, num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num


# 定义商品信息管理系统的类
class CargoSystem:

    system_version = "1.0"
    system_name = "商品管理系统"

    def __init__(self):
        # 系统初始化逻辑（商品列表）
        self.goods_list = []

    # 添加商品
    def add_goods(self):
        name = input("请输入商品的名字:")
        for s in self.goods_list:
            if s.name == name:
                print("该商品已存在!添加失败")
                return

        # 接收商品信息
        price = float(input("请输入商品价格:"))
        num = int(input("请输入商品数量:"))
        goss = Goods(name,price,num)
        self.goods_list.append(goss)


    # 修改商品
    def modify_goods(self):
        name = input("请输入商品的名字:")
        for s in self.goods_list:
            if s.name == name:
                price = float(input("请输入商品价格:"))
                num = int(input("请输入商品数量:"))
                goss = Goods(name, price, num)
                self.modify_goods.append(goss)
                print(f"{s}")
            else:
                print("商品不存在!修改失败!")

    # 删除商品
    def delete_goods(self):
        name = input("请输入商品的名字:")
        for s in self.goods_list:
            if s.name == name:
                self.goods_list.remove(s)
            else:
                print("商品不存在!删除失败!")

    # 查询商品
    def show_goods(self):
        name = input("请输入商品的名字:")
        for s in self.goods_list:
            if s.name == name:
                print(f"{s}")
            else:
                print("商品不存在!查询失败!")




# 菜单与主程序后续
    def run(self):
        while True:
            print(f"欢迎使用商品系统{CargoSystem.system_version}")
            print("#    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    ")
            print("#    #     1.添加商品      2.修改商品       3.删除商品        4.查询商品           5.退出系统    #    ")
            print("#    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #    ")

            choice  = input("请输入程序选项(1-5):")
            match choice:
                case "1":
                    self.add_goods()
                case "2":
                    self.modify_goods()
                case "3":
                    self.delete_goods()
                case "4":
                    self.show_goods()
                case "5":
                    print("bye~")
                    break
                case _:
                    print("操作错误,请选择1-5")

if __name__ == "__main__":
    shop_googs = CargoSystem()
    shop_googs.run()




# 采用面向对象的编程思想,开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据,通过控制台菜单与用户交互。具体功能如下:

# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来,格式为:"商品名称:xxx,商品价格:xxx,商品数量:xxx"。
# 5.退出购物车

# 定义商品类
class Goods:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称：{self.name} | 商品价格：{self.price} | 商品数量：{self.num}"

    # 商品的修改方法
    def update_goods(self, price=None, num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num


# 定义商品信息管理系统的类
class CargoSystem:
    system_version = "1.0"
    system_name = "商品管理系统"

    def __init__(self):
        self.goods_list = []   # 存储商品对象的列表

    # 添加商品
    def add_goods(self):
        name = input("请输入商品名称: ")
        # 检查是否已存在
        for goods in self.goods_list:
            if goods.name == name:
                print("该商品已存在！添加失败")
                return
        price = float(input("请输入商品价格: "))
        num = int(input("请输入商品数量: "))
        new_goods = Goods(name, price, num)
        self.goods_list.append(new_goods)
        print("商品添加成功！")

    # 修改商品
    def modify_goods(self):
        name = input("请输入要修改的商品名称: ")
        for goods in self.goods_list:
            if goods.name == name:
                price = float(input("请输入新的商品价格: "))
                num = int(input("请输入新的商品数量: "))
                goods.update_goods(price, num)   # 直接调用商品对象的方法修改
                print("商品修改成功！")
                return
        # 循环结束未找到
        print("商品不存在！修改失败")

    # 删除商品
    def delete_goods(self):
        name = input("请输入要删除的商品名称: ")
        for goods in self.goods_list:
            if goods.name == name:
                self.goods_list.remove(goods)
                print("商品删除成功！")
                return
        print("商品不存在！删除失败")

    # 查询商品（根据名称查询单个商品）
    def show_goods(self):
        name = input("请输入要查询的商品名称: ")
        for goods in self.goods_list:
            if goods.name == name:
                print(goods)   # 自动调用 __str__ 方法
                return
        print("商品不存在！查询失败")

    # 菜单与主程序
    def run(self):
        while True:
            print(f"\n欢迎使用{CargoSystem.system_name} v{CargoSystem.system_version}")
            print("#" * 50)
            print("#    1.添加商品      2.修改商品      3.删除商品      #")
            print("#    4.查询商品      5.退出系统                      #")
            print("#" * 50)
            choice = input("请输入操作选项(1-5): ")
            match choice:
                case "1":
                    self.add_goods()
                case "2":
                    self.modify_goods()
                case "3":
                    self.delete_goods()
                case "4":
                    self.show_goods()
                case "5":
                    print("感谢使用，再见！")
                    break
                case _:
                    print("输入错误，请重新输入1-5之间的数字！")


if __name__ == "__main__":
    shop_system = CargoSystem()
    shop_system.run()