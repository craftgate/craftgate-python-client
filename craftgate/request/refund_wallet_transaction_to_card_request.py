from decimal import Decimal
from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class RefundWalletTransactionToCardRequest(BaseRequest):
    def __init__(self, refund_price: Optional[Decimal] = None) -> None:
        self.refund_price = refund_price
