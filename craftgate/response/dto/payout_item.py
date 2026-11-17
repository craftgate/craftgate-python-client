from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.merchant_type import MerchantType
from craftgate.model.payout_item_subject import PayoutItemSubject
from craftgate.model.transaction_payout_status import TransactionPayoutStatus


class PayoutItem(object):
    def __init__(
            self,
            subject: Optional[PayoutItemSubject] = None,
            subject_id: Optional[int] = None,
            merchant_type: Optional[MerchantType] = None,
            merchant_id: Optional[int] = None,
            payout_amount: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            payout_status: Optional[TransactionPayoutStatus] = None,
            payout_date: Optional[datetime] = None,
            created_date: Optional[datetime] = None
    ) -> None:
        self.subject = subject
        self.subject_id = subject_id
        self.merchant_type = merchant_type
        self.merchant_id = merchant_id
        self.payout_amount = payout_amount
        self.currency = currency
        self.payout_status = payout_status
        self.payout_date = payout_date
        self.created_date = created_date
