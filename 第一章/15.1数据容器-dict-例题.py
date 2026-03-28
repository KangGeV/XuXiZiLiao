# 开发一个购物车管理系统,实现商品信息的添加、修改、删除余、查询功能。系统使用字典结构存储商品数据
# 通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来,格式为:"商品名称:xxx,商品价格:xxx,商品数量:xxx"。
# 5.退出购物车

shopping_cart={"Meta80":{"price":6999,"num":2},"鼠标":{...}}
#交互系统
print("欢迎使用购物车交互系统")
M = """
#####################
#    1.添加购物车     #
#    2.修改购物车     #
#    3.删除购物车     #
#    4.查询购物车     #
#    5.退出购物车     #
#####################
"""
print(M)

while True:
        #接收需要的操作
        A = input("请输入需要的操作(1-5):")

        match A:
            #添加购物车
            case 1:
                B = input("请输入需要添加的物品:")
                C = float(input("请输入商品的价格"))
                D = int(input("请输入商品的数量:"))
                if B in shopping_cart:
                    print("改商品已存在,请重新输入!")
                else:
                    shopping_cart[B] ={"prince" : C,"num": D}
            #修改购物车
            case 2:
                B = input("请输入需要添加的物品:")
                C = float(input("请输入商品的价格"))
                D = int(input("请输入商品的数量:"))
                if B not in shopping_cart:
                    print("改商品不存在,请重新输入!")
                else:
                    shopping_cart[B] = {"prince": C, "num": D}
            #删除购物车
            case 3:
                B = input("请输入需要添加的物品:")
                if B not in shopping_cart:
                    print("改商品不存在,请重新输入!")
                else:
                    del shopping_cart[B]
            #查询购物车
            case 4:
                for B in shopping_cart.keys():
                    E = shopping_cart[B]
                    print(f"商品名称:{B},商品价格:[{E['prince']},{E['num']}]",)
            #退出购物车
            case 5:
                print("bye~~~")
                break

            case _:

              print("操作异常,请重新操作!!!")



#------------------------------------------------优化后--------------------------------------------------------

# 购物车字典：商品名 -> {"price": 价格, "num": 数量}

shopping_cart = {}

print("欢迎使用购物车交互系统")
menu = """
#####################
#    1.添加购物车     #
#    2.修改购物车     #
#    3.删除购物车     #
#    4.查询购物车     #
#    5.退出购物车     #
#####################
"""
print(menu)

while True:
    option = input("请输入需要的操作(1-5): ")

    match option:
        # 添加购物车
        case "1":
            name = input("请输入需要添加的商品名称: ")
            price = float(input("请输入商品的价格: "))
            quantity = int(input("请输入商品的数量: "))
            if name in shopping_cart:
                print("该商品已存在，请使用修改功能或重新输入！")
            else:
                shopping_cart[name] = {"price": price, "num": quantity}
                print(f"商品 {name} 添加成功！")

        # 修改购物车
        case "2":
            name = input("请输入需要修改的商品名称: ")
            if name not in shopping_cart:
                print("该商品不存在，请先添加！")
            else:
                price = float(input("请输入新的价格: "))
                quantity = int(input("请输入新的数量: "))
                shopping_cart[name] = {"price": price, "num": quantity}
                print(f"商品 {name} 修改成功！")

        # 删除购物车
        case "3":
            name = input("请输入需要删除的商品名称: ")
            if name not in shopping_cart:
                print("该商品不存在，无法删除！")
            else:
                del shopping_cart[name]
                print(f"商品 {name} 删除成功！")

        # 查询购物车
        case "4":
            if not shopping_cart:
                print("购物车为空！")
            else:
                print("当前购物车商品：")
                for name, info in shopping_cart.items():
                    print(f"商品名称: {name}, 商品价格: {info['price']}, 商品数量: {info['num']}")

        # 退出购物车
        case "5":
            print("bye~~~")
            break

        case _:
            print("操作异常，请重新操作(1-5)！")
