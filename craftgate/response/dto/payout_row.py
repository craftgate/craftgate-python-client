from datetime import datetime
from decimal import Decimal
from typing import Optional


class PayoutRow(object):
    def __init__(
            self,
            name: Optional[str] = None,
            iban: Optional[str] = None,
            payout_id: Optional[int] = None,
            settlement_row_id: Optional[int] = None,
            merchant_id: Optional[int] = None,
            merchant_type: Optional[str] = None,
            payout_amount: Optional[Decimal] = None,
            payout_date: Optional[datetime] = None
    ):
        self.name = name
        self.iban = iban
        self.payout_id = payout_id
        self.settlement_row_id = settlement_row_id
        self.merchant_id = merchant_id
        self.merchant_type = merchant_type
        self.payout_amount = payout_amount
        self.payout_date = payout_date
