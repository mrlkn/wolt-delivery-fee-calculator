from datetime import datetime

from pydantic import BaseModel, Field, PositiveInt, conint

from config import delivery_conf


class Order(BaseModel):
    """
    Model to validate orders that used in delivery_fee_calc endpoint.
    """
    cart_value: PositiveInt = Field(
        description="Value of the shopping cart in cents."
    )
    delivery_distance: PositiveInt = Field(
        description="The distance between the store and customer’s location in meters."
    )
    amount_of_items: PositiveInt = Field(
        description="The amount of items in the customer's shopping cart."
    )
    time: datetime

    def is_free_of_delivery_fee(self) -> bool:
        """
        Returns True if cart value is equal or higher than 10000 (free_of_charge_value).
        Which means it is free to deliver.

        :return: bool
        """
        if self.cart_value >= delivery_conf.free_of_charge_cart_value:
            return True

    def is_rush_time(self) -> bool:
        """
        Returns True if order time is between rush times. (Friday 15:00 - 19:00)

        :return: bool
        """
        if self.time.weekday() == 4 and 15 >= self.time.hour >= 19:
            return True


class ResponseModel(BaseModel):
    """
    Basic response model to return delivery fee in cents.
    Delivery Fee can not be lower than 0 (base_delivery_fee) and can not be greater than 1500 (maximum_delivery_fee).
    """
    delivery_fee: conint(ge=delivery_conf.base_delivery_fee, le=delivery_conf.maximum_delivery_fee) = Field(
        description="Calculated delivery fee in cents."
    )
