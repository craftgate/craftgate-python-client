from datetime import datetime
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.refund_status import RefundStatus


class SearchPaymentTransactionRefundsRequest(object):
    def __init__(
            self,
            page=None,  # type: Optional[int]
            size=None,  # type: Optional[int]
            id=None,  # type: Optional[int]
            payment_id=None,  # type: Optional[int]
            payment_transaction_id=None,  # type: Optional[int]
            buyer_member_id=None,  # type: Optional[int]
            conversation_id=None,  # type: Optional[str]
            status=None,  # type: Optional[RefundStatus]
            currency=None,  # type: Optional[Currency]
            min_refund_price=None,  # type: Optional[Decimal]
            max_refund_price=None,  # type: Optional[Decimal]
            is_after_settlement=None,  # type: Optional[bool]
            min_created_date=None,  # type: Optional[datetime]
            max_created_date=None  # type: Optional[datetime]
    ):
        self.page = page
        self.size = size
        self.id = id
        self.payment_id = payment_id
        self.payment_transaction_id = payment_transaction_id
        self.buyer_member_id = buyer_member_id
        self.conversation_id = conversation_id
        self.status = status
        self.currency = currency
        self.min_refund_price = min_refund_price
        self.max_refund_price = max_refund_price
        self.is_after_settlement = is_after_settlement
        self.min_created_date = min_created_date
        self.max_created_date = max_created_date
