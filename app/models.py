from datetime import datetime

from pydantic import BaseModel, Field, PositiveInt, conint


class Order(BaseModel):
    """
    Model to validate orders that used in delivery_fee_calc endpoint.
    """
    cart_value: PositiveInt = Field(
        alias="Cart Value",
        description="Value of the shopping cart in cents."
    )
    delivery_distance: PositiveInt = Field(
        alias="Delivery Distance",
        description="The distance between the store and customer’s location in meters."
    )
    amount_of_items: PositiveInt = Field(
        alias="Amount of Items",
        description="The amount of items in the customer's shopping cart."
    )
    time: datetime


class ResponseModel(BaseModel):
    """
    Basic response model to return delivery fee. Delivery Fee can not be less than 0 and can not be greater than 15.
    """
    delivery_fee: conint(ge=0, le=15) = Field(
        alias="Delivery Fee",
        description="Calculated delivery fee in cents."
    )
