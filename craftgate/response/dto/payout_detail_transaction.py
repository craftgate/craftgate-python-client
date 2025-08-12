from typing import Optional


class PayoutDetailTransaction(object):
    def __init__(
        self,
        transaction_id=None,     # type: Optional[int]
        transaction_type=None,   # type: Optional[str]
        payout_amount=None       # type: Optional[float]
    ):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.payout_amount = payout_amount
