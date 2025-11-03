from datetime import datetime
from typing import Optional

from craftgate.model.transaction_payout_status import TransactionPayoutStatus


class PayoutStatus(object):
    def __init__(
            self,
            merchant_status: Optional[TransactionPayoutStatus] = None,
            merchant_status_date: Optional[datetime] = None,
            sub_merchant_member_status: Optional[TransactionPayoutStatus] = None,
            sub_merchant_member_status_date: Optional[datetime] = None
    ):
        self.merchant_status = merchant_status
        self.merchant_status_date = merchant_status_date
        self.sub_merchant_member_status = sub_merchant_member_status
        self.sub_merchant_member_status_date = sub_merchant_member_status_date
