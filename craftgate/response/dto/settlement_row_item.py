from decimal import Decimal
from typing import Optional

from craftgate.model.settlement_row_item_subject import SettlementRowItemSubject


class SettlementRowItem(object):
    def __init__(
            self,
            subject: Optional[SettlementRowItemSubject] = None,
            subject_id: Optional[int] = None,
            payment_transaction_id: Optional[int] = None,
            payout_amount: Optional[Decimal] = None
    ) -> None:
        self.subject = subject
        self.subject_id = subject_id
        self.payment_transaction_id = payment_transaction_id
        self.payout_amount = payout_amount
