from fastapi import FastAPI

from config import delivery_conf
from calculations import calculate_total_delivery_fee
from models import ResponseModel, Order

app = FastAPI()


@app.post("/calc_delivery_fee/", response_model=ResponseModel, summary="Calculate delivery fee based on request body")
def calc_delivery_fee(order: Order) -> ResponseModel:
    """
    Calculate delivery fee based on the fields of the Order model.

    Gets an Order model as request body and does validations according to it. After that, calculates fee based on the
    order data.
    :param order: Order Model
    :return: HttpResponse
    """
    delivery_fee = delivery_conf.base_delivery_fee

    if order.is_free_of_delivery_fee():
        return ResponseModel(delivery_fee=delivery_fee)

    delivery_fee = calculate_total_delivery_fee(order.delivery_distance, order.amount_of_items, order.cart_value)

    if order.is_rush_time():
        delivery_fee += delivery_fee * delivery_conf.rush_time_multiplier

    if delivery_fee >= delivery_conf.maximum_delivery_fee:
        delivery_fee = delivery_conf.maximum_delivery_fee

    return ResponseModel(delivery_fee=delivery_fee)
