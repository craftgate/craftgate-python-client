from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from craftgate.model.multi_payment_status import MultiPaymentStatus


class MultiPaymentResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            multi_payment_status: Optional[MultiPaymentStatus] = None,
            token: Optional[str] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            paid_price: Optional[Decimal] = None,
            remaining_amount: Optional[Decimal] = None,
            token_expire_date: Optional[datetime] = None,
            payment_ids: Optional[List[int]] = None
    ) -> None:
        self.id = id
        self.multi_payment_status = multi_payment_status
        self.token = token
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.paid_price = paid_price
        self.remaining_amount = remaining_amount
        self.token_expire_date = token_expire_date
        self.payment_ids = payment_ids
