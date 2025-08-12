from typing import Optional
from craftgate.model.refund_destination_type import RefundDestinationType

class RefundPaymentRequest(object):
    def __init__(
        self,
        payment_id=None,                         # type: Optional[int]
        conversation_id=None,                    # type: Optional[str]
        refund_destination_type=RefundDestinationType.PROVIDER,  # type: RefundDestinationType
        charge_from_me=False                     # type: bool
    ):
        self.payment_id = payment_id
        self.conversation_id = conversation_id
        self.refund_destination_type = refund_destination_type
        self.charge_from_me = charge_from_me