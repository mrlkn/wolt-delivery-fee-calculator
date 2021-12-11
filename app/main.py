from fastapi import FastAPI

from calculations import calculate_total_delivery_fee
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
    rush_time_multiplier = 0.1

    if order.is_free_of_delivery_fee():
        return ResponseModel(delivery_fee=delivery_fee)

    delivery_fee = calculate_total_delivery_fee(order.delivery_distance, order.amount_of_items, order.cart_value)

    if order.is_rush_time():
        delivery_fee += delivery_fee * rush_time_multiplier

    if delivery_fee >= maximum_delivery_fee:
        delivery_fee = maximum_delivery_fee

    return ResponseModel(delivery_fee=delivery_fee)
