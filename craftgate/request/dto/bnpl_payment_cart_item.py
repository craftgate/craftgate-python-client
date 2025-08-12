from typing import Optional

from decimal import Decimal
from craftgate.model.bnpl_cart_item_type import BnplCartItemType


class BnplPaymentCartItem(object):
    def __init__(
            self,
            id: Optional[str] = None,
            name: Optional[str] = None,
            brand_name: Optional[str] = None,
            type: Optional[BnplCartItemType] = None,
            unit_price: Optional[Decimal] = None,
            quantity: Optional[int] = None
    ) -> None:
        self.id = id
        self.name = name
        self.brand_name = brand_name
        self.type = type
        self.unit_price = unit_price
        self.quantity = quantity
