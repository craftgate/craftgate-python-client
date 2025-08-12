from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.status import Status
from craftgate.model.currency import Currency
from craftgate.model.transaction_payout_status import TransactionPayoutStatus


class WithdrawResponse(object):
    def __init__(
        self,
        id=None,  # type: Optional[int]
        created_date=None,  # type: Optional[datetime]
        status=None,  # type: Optional[Status]
        price=None,  # type: Optional[Decimal]
        description=None,  # type: Optional[str]
        currency=None,  # type: Optional[Currency]
        payout_status=None,  # type: Optional[TransactionPayoutStatus]
        member_id=None,  # type: Optional[int]
        payout_id=None  # type: Optional[int]
    ):
        self.id = id
        self.created_date = created_date
        self.status = status
        self.price = price
        self.description = description
        self.currency = currency
        self.payout_status = payout_status
        self.member_id = member_id
        self.payout_id = payout_id
