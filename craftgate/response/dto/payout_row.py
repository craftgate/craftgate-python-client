from typing import Optional
from datetime import datetime


class PayoutRow(object):
    def __init__(
        self,
        name=None,            # type: Optional[str]
        iban=None,            # type: Optional[str]
        payout_id=None,       # type: Optional[int]
        merchant_id=None,     # type: Optional[int]
        merchant_type=None,   # type: Optional[str]
        payout_amount=None,   # type: Optional[float]
        payout_date=None      # type: Optional[datetime]
    ):
        self.name = name
        self.iban = iban
        self.payout_id = payout_id
        self.merchant_id = merchant_id
        self.merchant_type = merchant_type
        self.payout_amount = payout_amount
        self.payout_date = payout_date
