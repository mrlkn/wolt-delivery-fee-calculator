from pydantic import BaseModel, Field


class Config(BaseModel):
    """
    Config that based to the delivery fee calculations.
    """
    base_delivery_fee: int = Field(description="Base Delivery Fee")
    minimum_distance_fee: int = Field(description="Minimum distance fee in cents")
    distance_to_charge: int = Field(description="Each additional distance to charge in meters")
    charge_free_item_count: int = Field(description="Free to deliver item count")
    cart_value_to_fulfill: int = Field(description="Cart value to fulfill with delivery fee")
    maximum_delivery_fee: int = Field(description="Maximum amount of delivery fee")
    rush_time_multiplier: float = Field(description="Delivery fee multiplier in the rush time")
    free_of_charge_cart_value: int = Field(description="Cart value that is free of any delivery fee")


delivery_conf = Config(
    base_delivery_fee=0,
    minimum_distance_fee=200,
    distance_to_charge=500,
    charge_free_item_count=4,
    cart_value_to_fulfill=1000,
    maximum_delivery_fee=1500,
    rush_time_multiplier=0.1,
    free_of_charge_cart_value=10000
)
