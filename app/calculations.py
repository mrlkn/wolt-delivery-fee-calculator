def calculate_distance_fee(order_distance: int) -> int:
    """
    Calculates the fee based on the distance in order with a mathematical solution.

    Calculating how many 500 meters are there in the total distance and rounding it up the one higher integer.
    i.e. 1501/500 is 3.002 and fee should be 4 Euro so we are rounding it up.
    However, the minimum fee is 2 Euros so if we have cost_ratio lower than two we should return two anyways.

    :param order_distance: integer distance of the order
    :return: fee of the distance
    """
    cost_ratio = int((order_distance / 500) + (order_distance % 5 > 0))

    if cost_ratio <= 2:
        return 2
    return cost_ratio


def calculate_item_fee(items_in_order: int) -> float:
    """
    Calculates the fee based on the item in order with a mathematical solution.

    If there are less or equal item than 4 there is no fee. For each item that are more than 4, we are adding 50 cents
    which is equal of dividing the item count by 2.
    i.e. there are 7 items and 3 of them is excessive. 3/2 is equal of 1.5 Euro fee.

    :param items_in_order: integer items of the order
    :return: surplus fee of the items
    """
    free_of_charge_item = 4

    if items_in_order <= free_of_charge_item:
        return 0

    excessive_item_count = items_in_order - free_of_charge_item

    fee = excessive_item_count / 2
    return fee


def calculate_cart_value_fee(cart_value: int) -> float:
    """
    Calculates the fee based on the cart value.

    If cart value is higher than 10 euros (1000 cents) there is no delivery fee. However, if the cart value is lower
    than it cart value is rounded up to 10 with fee included.
    i.e. cart value is 790 so we round it up to 1000 with 110 as a delivery fee. Then finally converts it to euros by
    dividing it to 10.

    :param cart_value: integer cart value of the order
    :return: fee that rounds the cart value to the 10
    """
    fee = 0
    free_of_charge = 1000

    if cart_value > free_of_charge:
        return fee

    fee = free_of_charge - cart_value
    fee_in_euros = fee / 100

    return fee_in_euros
