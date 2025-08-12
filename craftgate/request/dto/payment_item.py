import decimal
from decimal import Decimal
from typing import Optional


class PaymentItem:
    def __init__(
            self,
            name: Optional[str] = None,
            price: Optional[decimal] = None,
            external_id: Optional[str] = None,
            sub_merchant_member_id: Optional[int] = None,
            sub_merchant_member_price: Optional[decimal] = None
    ) -> None:
        self.name = name
        self.price = price
        self.external_id = external_id
        self.sub_merchant_member_id = sub_merchant_member_id
        self.sub_merchant_member_price = sub_merchant_member_price
