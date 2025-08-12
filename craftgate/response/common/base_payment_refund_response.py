from datetime import datetime
from decimal import Decimal
from typing import Any, Optional

from craftgate.model.refund_destination_type import RefundDestinationType
from craftgate.model.refund_status import RefundStatus


class BasePaymentRefundResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            created_date: Optional[datetime] = None,
            status: Optional[RefundStatus] = None,
            refund_destination_type: Optional[RefundDestinationType] = None,
            refund_price: Optional[Decimal] = None,
            refund_bank_price: Optional[Decimal] = None,
            refund_wallet_price: Optional[Decimal] = None,
            conversation_id: Optional[str] = None,
            auth_code: Optional[str] = None,
            host_reference: Optional[str] = None,
            trans_id: Optional[str] = None,
            payment_id: Optional[int] = None,
            **kwargs: Any
    ) -> None:
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
