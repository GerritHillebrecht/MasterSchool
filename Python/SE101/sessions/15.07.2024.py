def add_tax(price):
    """
    Compute the final price after tax for pices above $ 100 - careful though, for products with prices < 100 the function returns wrong results
    :param price: Float value above 100
    :return: Float value of tax added price
    """
    return price + (price-100) * 0.25

add_tax(20)