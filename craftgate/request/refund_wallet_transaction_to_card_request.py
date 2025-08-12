from decimal import Decimal
from typing import Optional


class RefundWalletTransactionToCardRequest(object):
    def __init__(self, refund_price: Optional[Decimal] = None) -> None:
        self.refund_price = refund_price
