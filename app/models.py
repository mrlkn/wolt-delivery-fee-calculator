from datetime import datetime

from pydantic import BaseModel, Field, PositiveInt, confloat


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
        Returns True if cart value is equal or higher than 100 Euro which means it is free of delivery fee.

        :return: bool
        """
        delivery_free_of_charge_amount = 10000
        if self.cart_value >= delivery_free_of_charge_amount:
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
    Basic response model to return delivery fee. Delivery Fee can not be less than 0 and can not be greater than 15.
    """
    delivery_fee: confloat(ge=0, le=15) = Field(
        description="Calculated delivery fee in cents."
    )
