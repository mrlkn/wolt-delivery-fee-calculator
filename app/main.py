from fastapi import FastAPI

from calculations import calculate_distance_fee, calculate_item_fee, calculate_cart_value_fee
from models import ResponseModel, Order

app = FastAPI()


@app.post(
    "/calc_delivery_fee/",
    response_model=ResponseModel,
    summary="Calculate delivery fee based on request body"
)
def calc_delivery_fee(order: Order) -> ResponseModel:
    """
    Calculate delivery fee based on the fields of the Order model.

    :param order: Order Model
    :return: HttpResponse
    """
    delivery_fee = 0
    maximum_delivery_fee = 15

    if order.is_free_of_delivery_fee():
        return ResponseModel(delivery_fee=delivery_fee)

    delivery_fee += calculate_cart_value_fee(order.cart_value)
    delivery_fee += calculate_distance_fee(order.delivery_distance)
    delivery_fee += calculate_item_fee(order.amount_of_items)

    if order.is_rush_time():
        delivery_fee += delivery_fee * 0.1

    if delivery_fee >= maximum_delivery_fee:
        delivery_fee = maximum_delivery_fee

    return ResponseModel(delivery_fee=delivery_fee)
