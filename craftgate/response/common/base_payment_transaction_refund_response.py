from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.refund_destination_type import RefundDestinationType
from craftgate.model.refund_status import RefundStatus


class BasePaymentTransactionRefundResponse(object):
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
            is_after_settlement: Optional[bool] = None,
            payment_transaction_id: Optional[int] = None
    ) -> None:
        self.id = id
        self.created_date = created_date
        self.status = RefundStatus(status) if status is not None else None
        self.refund_destination_type = (
            RefundDestinationType(refund_destination_type) if refund_destination_type is not None else None
        )
        self.refund_price = refund_price
        self.refund_bank_price = refund_bank_price
        self.refund_wallet_price = refund_wallet_price
        self.conversation_id = conversation_id
        self.auth_code = auth_code
        self.host_reference = host_reference
        self.trans_id = trans_id
        self.is_after_settlement = is_after_settlement
        self.payment_transaction_id = payment_transaction_id
