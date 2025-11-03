from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency


class WalletResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            created_date: Optional[datetime] = None,
            updated_date: Optional[datetime] = None,
            amount: Optional[Decimal] = None,
            withdrawal_amount: Optional[Decimal] = None,
            negative_amount_limit: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            member_id: Optional[int] = None
    ) -> None:
        self.id = id
        self.created_date = created_date
        self.updated_date = updated_date
        self.amount = amount
        self.withdrawal_amount = withdrawal_amount
        self.negative_amount_limit = negative_amount_limit
        self.currency = currency
        self.member_id = member_id
