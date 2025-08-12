from typing import Optional
from datetime import datetime
from decimal import Decimal

from craftgate.model.currency import Currency


class WalletResponse(object):
    def __init__(
        self,
        id=None,  # type: Optional[int]
        created_date=None,  # type: Optional[datetime]
        updated_date=None,  # type: Optional[datetime]
        amount=None,  # type: Optional[Decimal]
        withdrawal_amount=None,  # type: Optional[Decimal]
        negative_amount_limit=None,  # type: Optional[Decimal]
        currency=None,  # type: Optional[Currency]
        member_id=None  # type: Optional[int]
    ):
        self.id = id
        self.created_date = created_date
        self.updated_date = updated_date
        self.amount = amount
        self.withdrawal_amount = withdrawal_amount
        self.negative_amount_limit = negative_amount_limit
        self.currency = currency
        self.member_id = member_id
