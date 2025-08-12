from typing import Optional

from craftgate.model.bnpl_cart_item_type import BnplCartItemType


class BnplPaymentCartItem(object):
    def __init__(self,
                 id=None,  # type: Optional[str]
                 name=None,  # type: Optional[str]
                 brand_name=None,  # type: Optional[str]
                 type=None,  # type: Optional[BnplCartItemType]
                 unit_price=None,  # type: Optional[float]
                 quantity=None  # type: Optional[int]
                 ):
        self.id = id
        self.name = name
        self.brand_name = brand_name
        self.type = type
        self.unit_price = unit_price
        self.quantity = quantity
