from decimal import Decimal
from typing import Optional


class WalletTransactionRefundableAmountResponse(object):
    def __init__(self, refundable_amount: Optional[Decimal] = None) -> None:
        self.refundable_amount = refundable_amount
