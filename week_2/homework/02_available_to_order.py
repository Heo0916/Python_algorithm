shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # for i in orders:
    #     if not is_existing_target_number_binary(i, menus):
    #         return False
    # return True

    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True



# def is_existing_target_number_binary(target, array):
#     min = 0
#     max = len(array) - 1
#     find = (min + max) // 2
#
#     while min <= max:
#         if array[find] == target:
#             return True
#         elif array[find] < target:
#             min = find + 1
#         else:
#             max = find - 1
#         find = (min + max) // 2
#     return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)

