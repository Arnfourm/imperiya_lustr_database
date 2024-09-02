def price_changer(promotion_price, price):
    if promotion_price == ' ' or promotion_price is None:
        return price
    else:
        return promotion_price