shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


#비싼 가격을 높은 할인율로 할인받고 싶음.
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    user_coupons.sort(reverse=True)

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100-coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return round(max_discounted_price)
    # n = len(prices)
    # m = len(coupons)
    #
    # sum = 0
    # for i in range(m):
    #     sum += prices[i]*((100-coupons[i])*0.01)
    #
    # for i in range(m,n):
    #     sum += prices[i]
    #
    #
    # return round(sum)

print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
