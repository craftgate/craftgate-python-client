from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.status import Status
from craftgate.model.transaction_payout_status import TransactionPayoutStatus


class WithdrawResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            created_date: Optional[datetime] = None,
            status: Optional[Status] = None,
            price: Optional[Decimal] = None,
            description: Optional[str] = None,
            currency: Optional[Currency] = None,
            payout_status: Optional[TransactionPayoutStatus] = None,
            member_id: Optional[int] = None,
            payout_id: Optional[int] = None
    ) -> None:
        self.id = id
        self.created_date = created_date
        self.status = status
        self.price = price
        self.description = description
        self.currency = currency
        self.payout_status = payout_status
        self.member_id = member_id
        self.payout_id = payout_id
