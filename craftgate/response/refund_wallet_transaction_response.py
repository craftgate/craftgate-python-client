from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.refund_status import RefundStatus
from craftgate.model.wallet_transaction_refund_card_transaction_type import (
    WalletTransactionRefundCardTransactionType,
)
from craftgate.response.dto.payment_error import PaymentError


class RefundWalletTransactionResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            created_date: Optional[datetime] = None,
            refund_status: Optional[RefundStatus] = None,
            refund_price: Optional[Decimal] = None,
            auth_code: Optional[str] = None,
            host_reference: Optional[str] = None,
            trans_id: Optional[str] = None,
            transaction_id: Optional[int] = None,
            transaction_type: Optional[WalletTransactionRefundCardTransactionType] = None,
            payment_error: Optional[PaymentError] = None,
            wallet_transaction_id: Optional[int] = None
    ) -> None:
        self.id = id
        self.created_date = created_date
        self.refund_status = refund_status
        self.refund_price = refund_price
        self.auth_code = auth_code
        self.host_reference = host_reference
        self.trans_id = trans_id
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.payment_error = payment_error
        self.wallet_transaction_id = wallet_transaction_id
