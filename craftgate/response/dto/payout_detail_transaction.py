from decimal import Decimal
from typing import Optional


class PayoutDetailTransaction(object):
    def __init__(
            self,
            transaction_id: Optional[int] = None,
            transaction_type: Optional[str] = None,
            payout_amount: Optional[Decimal] = None
    ):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.payout_amount = payout_amount
