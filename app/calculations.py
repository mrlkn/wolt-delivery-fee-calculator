from config import delivery_conf


def calculate_distance_fee(order_distance: int) -> int:
    """
    Calculates the fee based on the distance in order with a mathematical solution.

    Calculating how many 500 (distance_to_charge) meters are there in order distance and rounding it up the one
    higher integer then converts it to the cents by multiplying it with 100.
    i.e. 1501/500 is 3.002 and fee should be 4 Euro so we are rounding it up to 4 and multiplying to get 400 cents.
    However, if the calculation is lower than the minimum_distance_fee we should return it anyways.

    :param order_distance: integer distance of the order
    :return: fee of the distance
    """
    delivery_fee = int((order_distance / delivery_conf.distance_to_charge) + (order_distance % 5 > 0)) * 100

    if delivery_fee <= delivery_conf.minimum_distance_fee:
        return delivery_conf.minimum_distance_fee

    return delivery_fee


def calculate_item_fee(order_items: int) -> int:
    """
    Calculates the fee based on the item in order with a mathematical solution.

    If there are less or equal item than 4 (charge_free_item_count) there is no fee. For each item that are more than 4,
    we are adding 50 cents.
    i.e. there are 7 items and 3 of them is excessive. 4 * 50 = 200 cents

    :param order_items: integer items of the order
    :return: surplus fee of the items
    """

    if order_items <= delivery_conf.charge_free_item_count:
        return 0

    excessive_item_count = order_items - delivery_conf.charge_free_item_count

    fee = excessive_item_count * 50
    return fee


def calculate_cart_value_fee(cart_value: int) -> int:
    """
    Calculates the fee based on the cart value.

    If cart value is higher than 1000 cents(cart_value_to_fulfill) there is no delivery fee.
    However, if the cart value is lower than it cart value must be fulfill to it with delivery fee included.
    i.e. cart value is 790 so we round it up to 1000 with 110 as a delivery fee.

    :param cart_value: integer cart value of the order
    :return: fee that rounds the cart value to the 1000
    """

    if cart_value > delivery_conf.cart_value_to_fulfill:
        return 0

    fee = delivery_conf.cart_value_to_fulfill - cart_value

    return fee


def calculate_total_delivery_fee(order_distance: int, order_items: int, order_value: int) -> int:
    """
    Calculate the total amount of delivery fee with the given parameters.

    :param order_distance: integer of order distance in meters
    :param order_items: integer of item count of the order
    :param order_value: integer of the value of cart
    :return: total delivery fee
    """
    delivery_fee = delivery_conf.base_delivery_fee

    delivery_fee += calculate_distance_fee(order_distance)
    delivery_fee += calculate_item_fee(order_items)
    delivery_fee += calculate_cart_value_fee(order_value)

    return delivery_fee
