from typing import Optional
from decimal import Decimal


class WalletTransactionRefundableAmountResponse(object):
    def __init__(self, refundable_amount=None):  # type: Optional[Decimal]
        self.refundable_amount = refundable_amount
