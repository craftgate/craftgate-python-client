from decimal import Decimal
from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class PostAuthPaymentRequest(BaseRequest):
    def __init__(self, paid_price: Optional[Decimal] = None) -> None:
        self.paid_price = paid_price
