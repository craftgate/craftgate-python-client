from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.transaction_payout_status import TransactionPayoutStatus


class SearchWithdrawsRequest(object):
    def __init__(
            self,
            member_id: Optional[int] = None,
            currency: Optional[Currency] = None,
            payout_status: Optional[TransactionPayoutStatus] = None,
            min_withdraw_price: Optional[Decimal] = None,
            max_withdraw_price: Optional[Decimal] = None,
            min_created_date: Optional[datetime] = None,
            max_created_date: Optional[datetime] = None,
            page: int = 0,
            size: int = 10
    ):
        self.member_id = member_id
        self.currency = currency
        self.payout_status = payout_status
        self.min_withdraw_price = min_withdraw_price
        self.max_withdraw_price = max_withdraw_price
        self.min_created_date = min_created_date
        self.max_created_date = max_created_date
        self.page = page
        self.size = size
