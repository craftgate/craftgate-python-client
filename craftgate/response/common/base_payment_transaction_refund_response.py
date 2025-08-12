from craftgate.model.refund_status import RefundStatus
from craftgate.model.refund_destination_type import RefundDestinationType


class BasePaymentTransactionRefundResponse(object):
    def __init__(
        self,
        id=None,
        created_date=None,
        status=None,
        refund_destination_type=None,
        refund_price=None,
        refund_bank_price=None,
        refund_wallet_price=None,
        conversation_id=None,
        auth_code=None,
        host_reference=None,
        trans_id=None,
        is_after_settlement=None,
        payment_transaction_id=None
    ):
        self.id = id
        self.created_date = created_date
        self.status = RefundStatus(status) if status else None
        self.refund_destination_type = RefundDestinationType(refund_destination_type) if refund_destination_type else None
        self.refund_price = refund_price
        self.refund_bank_price = refund_bank_price
        self.refund_wallet_price = refund_wallet_price
        self.conversation_id = conversation_id
        self.auth_code = auth_code
        self.host_reference = host_reference
        self.trans_id = trans_id
        self.is_after_settlement = is_after_settlement
        self.payment_transaction_id = payment_transaction_id