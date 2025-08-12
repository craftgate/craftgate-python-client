from decimal import Decimal
from typing import Optional


class PostAuthPaymentRequest(object):
    def __init__(self, paid_price: Optional[Decimal] = None) -> None:
        self.paid_price = paid_price
