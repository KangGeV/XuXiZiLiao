
# 案例
# 电商订单计算器
# 定义一个函数,用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费计算订单的总金额。
# 具体规则如下:
# 优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元元(且抵扣金额不能超过商品总价,积分只能整百抵扣)。
# goos(商品名,价格,数量)

def spjis(*goos,youhui=0,jifen=0,yunfei=0):
    """
    计算总金额
    :param goos: 商品信息
    :param youhui: 优惠信息
    :param jifen: 积分
    :param yunfei: 运费
    :return: 总金额
    """
    #计算商品金额
    total_jiage = (s[1]*s[2] for s in goos)#一个商品的
    total_quanbu = sum(total_jiage)
    #使用优惠券
    if total_quanbu >= 5000 and total_quanbu >= youhui:
        total_quanbu -= youhui
    #使用积分
    if total_quanbu >= 5000 and total_quanbu >= jifen //100:
        total_quanbu -= jifen//100
    #加运费
    total_quanbu += yunfei
    return total_quanbu

total = spjis(("鼠标",188,2),("键盘",388,1),("手机",6999,1),youhui=100,jifen=10,yunfei=9)
print(total)



# ==================================================优化===========================================================
# def calculate_total(*goods, coupon=0, points=0, shipping=0):
#     """
#     计算订单总金额
#     :param goods: 商品信息，每个商品为 (名称, 单价, 数量)
#     :param coupon: 优惠券金额（元）
#     :param points: 积分值（100积分=1元）
#     :param shipping: 运费（元）
#     :return: 订单总金额
#     """
#     # 计算商品总价
#     total_price = 0
#     for item in goods:
#         # item 应为 (name, price, quantity)
#         price, quantity = item[1], item[2]
#         total_price += price * quantity
#
#     # 保存原始总价用于条件判断
#     original_price = total_price
#
#     # 使用优惠券（需满5000且优惠券金额不超过商品总价）
#     if original_price >= 5000 and coupon <= total_price:
#         total_price -= coupon
#
#     # 使用积分抵扣（需满5000，且抵扣金额不超过商品总价，积分只能整百抵扣）
#     discount = points // 100   # 积分折算的抵扣金额
#     if original_price >= 5000 and discount <= total_price:
#         total_price -= discount
#
#     # 加上运费
#     total_price += shipping
#
#     return total_price
#
# # 示例调用
# result = calculate_total(
#     ("手机", 3000, 2),   # 商品1
#     ("充电器", 100, 1),  # 商品2
#     coupon=200,
#     points=500,          # 500积分 = 5元
#     shipping=10
# )
# print(f"订单总金额: {result}元")