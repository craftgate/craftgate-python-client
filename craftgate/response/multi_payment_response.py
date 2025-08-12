from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from craftgate.model.multi_payment_status import MultiPaymentStatus

class MultiPaymentResponse(object):
    def __init__(
        self,
        id=None,  # type: Optional[int]
        multi_payment_status=None,  # type: Optional[MultiPaymentStatus]
        token=None,  # type: Optional[str]
        conversation_id=None,  # type: Optional[str]
        external_id=None,  # type: Optional[str]
        paid_price=None,  # type: Optional[Decimal]
        remaining_amount=None,  # type: Optional[Decimal]
        token_expire_date=None,  # type: Optional[datetime]
        payment_ids=None  # type: Optional[List[int]]
    ):
        self.id = id
        self.multi_payment_status = multi_payment_status
        self.token = token
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.paid_price = paid_price
        self.remaining_amount = remaining_amount
        self.token_expire_date = token_expire_date
        self.payment_ids = payment_ids