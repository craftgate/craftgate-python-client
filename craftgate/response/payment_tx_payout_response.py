from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from craftgate.model.currency import Currency
from craftgate.model.payout_approval_status import PayoutApprovalStatus
from craftgate.response.dto.payout_item import PayoutItem


class PaymentTxPayoutResponse(object):
    def __init__(
            self,
            payment_transaction_id: Optional[int] = None,
            currency: Optional[Currency] = None,
            parity: Optional[Decimal] = None,
            approval_status: Optional[PayoutApprovalStatus] = None,
            approval_status_date: Optional[datetime] = None,
            blockage_resolved_date: Optional[datetime] = None,
            created_date: Optional[datetime] = None,
            payout_items: Optional[List[PayoutItem]] = None
    ) -> None:
        self.payment_transaction_id = payment_transaction_id
        self.currency = currency
        self.parity = parity
        self.approval_status = approval_status
        self.approval_status_date = approval_status_date
        self.blockage_resolved_date = blockage_resolved_date
        self.created_date = created_date
        self.payout_items = payout_items
