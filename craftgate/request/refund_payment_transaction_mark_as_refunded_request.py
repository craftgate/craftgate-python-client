from typing import Optional
from craftgate.model.refund_destination_type import RefundDestinationType

class RefundPaymentTransactionMarkAsRefundedRequest(object):
    def __init__(
        self,
        payment_transaction_id=None,             # type: Optional[int]
        conversation_id=None,                    # type: Optional[str]
        refund_price=None,                        # type: Optional[float]
        refund_destination_type=RefundDestinationType.PROVIDER,  # type: RefundDestinationType
        charge_from_me=False                     # type: bool
    ):
        self.payment_transaction_id = payment_transaction_id
        self.conversation_id = conversation_id
        self.refund_price = refund_price
        self.refund_destination_type = refund_destination_type
        self.charge_from_me = charge_from_me