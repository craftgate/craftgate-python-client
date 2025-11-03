from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.refund_status import RefundStatus


class SearchPaymentTransactionRefundsRequest(object):
    def __init__(
            self,
            page: Optional[int] = None,
            size: Optional[int] = None,
            id: Optional[int] = None,
            payment_id: Optional[int] = None,
            payment_transaction_id: Optional[int] = None,
            buyer_member_id: Optional[int] = None,
            conversation_id: Optional[str] = None,
            status: Optional[RefundStatus] = None,
            currency: Optional[Currency] = None,
            min_refund_price: Optional[Decimal] = None,
            max_refund_price: Optional[Decimal] = None,
            is_after_settlement: Optional[bool] = None,
            min_created_date: Optional[datetime] = None,
            max_created_date: Optional[datetime] = None
    ) -> None:
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
