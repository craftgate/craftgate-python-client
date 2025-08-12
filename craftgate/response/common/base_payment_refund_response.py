from typing import Optional
from datetime import datetime
from craftgate.model.refund_status import RefundStatus
from craftgate.model.refund_destination_type import RefundDestinationType


class BasePaymentRefundResponse(object):
    def __init__(
        self,
        id=None,  # type: Optional[int]
        created_date=None,  # type: Optional[datetime]
        status=None,  # type: Optional[RefundStatus]
        refund_destination_type=None,  # type: Optional[RefundDestinationType]
        refund_price=None,  # type: Optional[float]
        refund_bank_price=None,  # type: Optional[float]
        refund_wallet_price=None,  # type: Optional[float]
        conversation_id=None,  # type: Optional[str]
        auth_code=None,  # type: Optional[str]
        host_reference=None,  # type: Optional[str]
        trans_id=None,  # type: Optional[str]
        payment_id=None,  # type: Optional[int]
        **kwargs
    ):
        self.id = id
        self.created_date = created_date
        self.status = status
        self.refund_destination_type = refund_destination_type
        self.refund_price = refund_price
        self.refund_bank_price = refund_bank_price
        self.refund_wallet_price = refund_wallet_price
        self.conversation_id = conversation_id
        self.auth_code = auth_code
        self.host_reference = host_reference
        self.trans_id = trans_id
        self.payment_id = payment_id